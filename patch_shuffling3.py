with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if "async def start_auction" in line:
        skip = True
        new_logic = """    async def start_auction(self, all_cricket_players: List[dict]):
        \"\"\"Shuffle players and begin the auction with cheat sheet loaded between 100-140.\"\"\"
        if self.auction_active:
            return
            
        self.auction_active = True
        self.status = 'auction'
        
        cheat_names = [
            "Shikhar Dhawan", "Suresh Raina", "Gautam Gambhir", "Mayank Agarwal", "Keshav Maharaj",
            "Shane Watson", "Yuvraj Singh", "Jacques Kallis", "Abhishek Nayar",
            "Dinesh Karthik", "Aditya Tare",
            "Bhuvneshwar Kumar", "Amit Mishra", "Sandeep Sharma", "Harbhajan Singh"
        ]
        
        cheat_players = []
        regular_players = []
        
        for p in all_cricket_players:
            if p.get('name') in cheat_names:
                cheat_players.append(p)
            else:
                regular_players.append(p)
                
        # Sort regular players by rating
        regular_players = sorted(regular_players, key=lambda x: x.get('rating', 0), reverse=True)
        
        import random
        
        # Phase 1: First 100 players (0 to 99) -> Highest rated regular players
        phase1 = regular_players[:100]
        random.shuffle(phase1)
        
        # Phase 2: Picks 100 to 140 -> Next 25 regular players + 15 Cheat Players (Total 40)
        phase2_regulars = regular_players[100:125]
        phase2 = phase2_regulars + cheat_players
        random.shuffle(phase2)
        
        # Phase 3: Picks 140+ -> The rest
        phase3 = regular_players[125:]
        random.shuffle(phase3)
        
        # Combine
        self.cricket_players = phase1 + phase2 + phase3
        self.current_player_index = 0
        
        # Reset budgets and UI
"""
        out.append(new_logic)
        continue
        
    if skip and "def present_next_player" in line:
        # We need to insert the rest of start_auction that we skipped
        rest = """        for p in self.players.values():
            p["budget"] = 120.0
            
        budgets_data = {uid: 120.0 for uid in self.players.keys()}
        
        await self.broadcast({
            "type": "auction_start",
            "total_players": len(self.cricket_players),
            "budgets": budgets_data
        })
        
        await asyncio.sleep(1)
        await self.present_next_player()

"""
        out.append(rest)
        out.append(line)
        skip = False
        continue
        
    if not skip:
        out.append(line)

with open("game_engine.py", "w") as f:
    f.writelines(out)
