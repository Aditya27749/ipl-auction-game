import asyncio
import random
import logging
from typing import Dict, List, Optional
from models import update_room_status, update_player_budget, draft_player, get_drafted_players, update_team_score, get_all_drafted

logger = logging.getLogger(__name__)

class AuctionRoom:
    """Manages the state of one auction room"""
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.players: Dict[str, dict] = {} # {user_id: {"ws": websocket, "name": str, "budget": float}}
        self.cricket_players: List[dict] = []
        self.unsold_players: List[dict] = []
        self.current_player_index = -1
        self.current_bid = 0.0
        self.current_bidder: Optional[str] = None
        self.auction_active = False
        self.pick_order = 0
        self.bid_lock = asyncio.Lock()
        self.status = 'waiting'
        self.timer_task: Optional[asyncio.Task] = None
        self.timer_seconds = 15
        
    async def broadcast(self, message: dict):
        """Send message to all connected WebSocket clients."""
        dead_connections = []
        for user_id, p in self.players.items():
            if p["ws"]:
                try:
                    await p["ws"].send_json(message)
                except Exception as e:
                    logger.error(f"Error sending to {user_id}: {e}")
                    dead_connections.append(user_id)
                    
        for user_id in dead_connections:
            self.players[user_id]["ws"] = None

    async def sync_player_state(self, player_id: str):
        """Send the complete current state to a specific player."""
        player_info = self.players.get(player_id)
        if not player_info or not player_info["ws"]:
            return
            
        if self.auction_active:
            # 1. Start auction layout
            budgets_data = {uid: {"name": p["name"], "budget": p["budget"]} for uid, p in self.players.items()}
            try:
                await player_info["ws"].send_json({
                    "type": "auction_start",
                    "total_players": len(self.cricket_players),
                    "budgets": budgets_data
                })
                
                # 2. Current player
                if 0 <= self.current_player_index < len(self.cricket_players):
                    current_player = self.cricket_players[self.current_player_index]
                    await player_info["ws"].send_json({
                        "type": "new_player",
                        "player": current_player,
                        "index": self.current_player_index + 1,
                        "total": len(self.cricket_players)
                    })
                    
                    # 3. Current bid
                    if self.current_bidder:
                        bidder_name = self.players[self.current_bidder]["name"]
                        await player_info["ws"].send_json({
                            "type": "bid_update",
                            "bidder_name": bidder_name,
                            "amount": self.current_bid,
                            "bidder_id": self.current_bidder
                        })
                
                # 4. Current team stats
                team = get_drafted_players(self.room_id, player_id)
                normalized_team = []
                for t in team:
                    normalized_team.append({
                        "name": t.get("name", "Unknown"),
                        "role": t.get("role", "Unknown"),
                        "nationality": t.get("nationality", "Indian"),
                        "bought_price": t.get("price_paid", 0),
                        "ipl_team": t.get("ipl_team", ""),
                    })
                await player_info["ws"].send_json({
                    "type": "team_update",
                    "player_id": player_id,
                    "team": normalized_team,
                    "team_size": len(normalized_team)
                })
            except Exception as e:
                logger.error(f"Error syncing state to {player_id}: {e}")

    async def start_timer(self):
        if self.timer_task:
            self.timer_task.cancel()
        
        self.timer_seconds = 15
        self.timer_task = asyncio.create_task(self._timer_loop())

    async def _timer_loop(self):
        try:
            while self.timer_seconds > 0:
                await self.broadcast({"type": "timer_update", "seconds": self.timer_seconds})
                await asyncio.sleep(1)
                self.timer_seconds -= 1
            
            # Timer reached 0
            await self.broadcast({"type": "timer_update", "seconds": 0})
            await self.sell_player()
        except asyncio.CancelledError:
            pass

    async def start_auction(self, all_cricket_players: List[dict]):
        """Shuffle players and begin the auction."""
        if self.auction_active:
            return
            
        self.auction_active = True
        self.status = 'auction'
        self.cricket_players = all_cricket_players.copy()
        random.shuffle(self.cricket_players)
        
        self.current_player_index = -1
        update_room_status(self.room_id, 'auction')
        
        # Send initial budgets along with auction start
        budgets_data = {}
        for uid, p in self.players.items():
            budgets_data[uid] = {"name": p["name"], "budget": p["budget"]}
        
        await self.broadcast({
            "type": "auction_start",
            "total_players": len(self.cricket_players),
            "budgets": budgets_data
        })
        
        await asyncio.sleep(1)
        await self.present_next_player()

    async def present_next_player(self):
        """Present the next player for auction."""
        self.current_player_index += 1
        
        # Check if all teams are full or all players presented
        all_teams_full = all(
            len(get_drafted_players(self.room_id, uid)) >= 12
            for uid in self.players
        )
        
        if all_teams_full:
            await self.end_auction()
            return
            
        if self.current_player_index >= len(self.cricket_players):
            if self.unsold_players:
                self.cricket_players.extend(self.unsold_players)
                self.unsold_players = []
            else:
                await self.end_auction()
                return
            
        current_player = self.cricket_players[self.current_player_index]
        self.current_bid = current_player['base_price']
        self.current_bidder = None
        
        await self.broadcast({
            "type": "new_player",
            "player": current_player,
            "index": self.current_player_index + 1,
            "total": len(self.cricket_players)
        })
        await self.start_timer()

    async def place_bid(self, user_id: str, amount: float):
        """Process a bid with full validation and race condition protection."""
        async with self.bid_lock:
            if not self.auction_active:
                return False, "Auction is not active"
                
            if self.current_player_index < 0 or self.current_player_index >= len(self.cricket_players):
                return False, "No active player being auctioned"
                
            player_info = self.players.get(user_id)
            if not player_info:
                return False, "Player not in room"
            
            # Must be higher than current bid (or equal to base if first bid)
            if self.current_bidder is not None and amount <= self.current_bid:
                return False, f"Bid must be higher than ₹{self.current_bid} CR"
            
            if self.current_bidder is None and amount < self.current_bid:
                return False, f"Bid must be at least ₹{self.current_bid} CR (base price)"
                
            if amount > player_info["budget"]:
                return False, f"Not enough budget! You have ₹{player_info['budget']:.2f} CR"
                
            # Fetch user's current team from DB to validate roster constraints
            current_team = get_drafted_players(self.room_id, user_id)
            if len(current_team) >= 12:
                return False, "Roster is full (12 players max)"
                
            current_player = self.cricket_players[self.current_player_index]
            
            overseas_count = sum(1 for p in current_team if p.get('nationality', '').lower() != 'indian')
            if current_player.get('nationality', '').lower() != 'indian':
                if overseas_count >= 4:
                    return False, "Maximum 4 overseas players allowed"

            self.current_bid = amount
            self.current_bidder = user_id
            
            # Broadcast bid update with field names the frontend expects
            await self.broadcast({
                "type": "bid_update",
                "bidder_name": player_info["name"],
                "amount": amount,
                "bidder_id": user_id
            })
            await self.start_timer()
            
            return True, "Bid placed successfully"



    async def sell_player(self):
        """Finalize the sale of the current player."""
        if getattr(self, '_is_selling', False):
            return
        self._is_selling = True
        
        try:
            current_task = asyncio.current_task()
            if self.timer_task and self.timer_task != current_task:
                self.timer_task.cancel()
                
            if self.current_player_index < 0 or self.current_player_index >= len(self.cricket_players):
                await self.present_next_player()
                return
                
            current_player = self.cricket_players[self.current_player_index]
        
        if self.current_bidder:
            buyer_info = self.players[self.current_bidder]
            new_budget = buyer_info["budget"] - self.current_bid
            buyer_info["budget"] = new_budget
            
            update_player_budget(self.room_id, self.current_bidder, new_budget)
            
            self.pick_order += 1
            current_team = get_drafted_players(self.room_id, self.current_bidder)
            is_impact = (len(current_team) == 11)  # 12th player is impact
            
            draft_player(self.room_id, self.current_bidder, current_player["id"], 
                         self.current_bid, self.pick_order, is_impact)
                         
            # Send player_sold with fields matching frontend expectations
            await self.broadcast({
                "type": "player_sold",
                "player": current_player,
                "buyer_name": buyer_info["name"],
                "buyer_id": self.current_bidder,
                "amount": self.current_bid
            })
            
            # Send updated budgets to all players
            budgets_data = {}
            for uid, p in self.players.items():
                budgets_data[uid] = {"name": p["name"], "budget": p["budget"]}
            
            await self.broadcast({
                "type": "budget_update",
                "budgets": budgets_data
            })
            
            # Send team update to the buyer
            team = get_drafted_players(self.room_id, self.current_bidder)
            # Normalize team data for frontend
            normalized_team = []
            for t in team:
                normalized_team.append({
                    "name": t.get("name", "Unknown"),
                    "role": t.get("role", "Unknown"),
                    "nationality": t.get("nationality", "Indian"),
                    "bought_price": t.get("price_paid", 0),
                    "ipl_team": t.get("ipl_team", ""),
                })
            
            if buyer_info["ws"]:
                try:
                    await buyer_info["ws"].send_json({
                        "type": "team_update",
                        "player_id": self.current_bidder,
                        "team": normalized_team,
                        "team_size": len(normalized_team)
                    })
                except Exception:
                    pass
                
        else:
            await self.broadcast({
                "type": "player_unsold",
                "player": current_player
            })
            self.unsold_players.append(current_player)
            
        await asyncio.sleep(2.5)
        await self.present_next_player()
        
        except Exception as e:
            logger.error(f"Error in sell_player: {e}")
        finally:
            self._is_selling = False

    async def end_auction(self):
        """End the auction and calculate final scores."""
        if self.timer_task:
            self.timer_task.cancel()
            
        self.auction_active = False
        self.status = 'completed'
        update_room_status(self.room_id, 'completed')
        
        results = []
        for user_id, player_info in self.players.items():
            team = get_drafted_players(self.room_id, user_id)
            score = self.calculate_team_scores(team, player_info["budget"])
            update_team_score(self.room_id, user_id, score)
            
            # Normalize team for frontend
            normalized_team = []
            for t in team:
                normalized_team.append({
                    "name": t.get("name", "Unknown"),
                    "role": t.get("role", "Unknown"),
                    "nationality": t.get("nationality", "Indian"),
                    "bought_price": t.get("price_paid", 0),
                    "ipl_team": t.get("ipl_team", ""),
                    "rating": t.get("rating", 5.0),
                })
            
            results.append({
                "user_id": user_id,
                "player_name": player_info["name"],
                "score": score,
                "team": normalized_team,
                "team_size": len(normalized_team),
                "budget_remaining": round(player_info["budget"], 2)
            })
            
        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        
        await self.broadcast({
            "type": "auction_end",
            "results": results
        })

    def calculate_team_scores(self, team: List[dict], remaining_budget: float) -> float:
        """Calculate team score out of 10 based on multiple criteria."""
        if not team:
            return 0.0
            
        score = 0.0
        roles = {'Batsman': 0, 'Bowler': 0, 'All-Rounder': 0, 'Wicket-Keeper': 0}
        total_rating = 0.0
        overseas_count = 0
        max_rating = 0.0
        total_runs = 0
        total_wickets = 0
        
        for p in team:
            role = p.get('role', 'Batsman')
            if role in roles:
                roles[role] += 1
            else:
                roles['Batsman'] += 1
                
            rating = p.get('rating', 5.0)
            total_rating += rating
            if rating > max_rating:
                max_rating = rating
            if p.get('nationality', '').lower() != 'indian':
                overseas_count += 1
                
            total_runs += p.get('runs', 0)
            total_wickets += p.get('wickets', 0)

        # 1. Role Balance (2.0 pts)
        if roles.get('Wicket-Keeper', 0) >= 1:
            score += 0.5
        if 3 <= roles.get('Batsman', 0) <= 5:
            score += 0.5
        if 3 <= roles.get('Bowler', 0) <= 5:
            score += 0.5
        if 1 <= roles.get('All-Rounder', 0) <= 3:
            score += 0.5

        # 2. Star Power (2.5 pts)
        avg_rating = total_rating / len(team)
        score += (avg_rating / 10.0) * 2.5

        # 3. Budget Efficiency (1.5 pts)
        if len(team) == 12:
            score += 0.5
        efficiency = 1.0 - (remaining_budget / 100.0)
        score += max(0, min(1.0, efficiency))

        # 4. Team Composition (2.0 pts)
        if overseas_count <= 4:
            score += 0.5
        if len(team) == 12:
            score += 0.5
        if max_rating >= 8.0:
            score += 0.5
        if roles.get('Batsman', 0) > 0 and roles.get('Bowler', 0) > 0:
            score += 0.5

        # 5. Statistical Power (2.0 pts)
        max_possible_runs = 30000 
        max_possible_wickets = 1000
        
        runs_score = (total_runs / max_possible_runs) * 1.0
        wickets_score = (total_wickets / max_possible_wickets) * 1.0
        score += min(1.0, runs_score) + min(1.0, wickets_score)

        return round(min(10.0, score), 2)
