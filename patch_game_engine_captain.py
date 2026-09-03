import re

with open("game_engine.py", "r") as f:
    code = f.read()

# 1. Update start_auction to assign teams and captains
start_patch = """        # Assign teams and secret captains
        franchises = ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Rajasthan Royals", "Sunrisers Hyderabad", "Delhi Capitals", "Punjab Kings", "Gujarat Titans", "Lucknow Super Giants"]
        import random
        random.shuffle(franchises)
        
        top_players = sorted(all_cricket_players, key=lambda x: x.get('rating', 0), reverse=True)[:50]
        captain_names = [p['name'] for p in top_players]
        random.shuffle(captain_names)
        
        for i, (uid, p) in enumerate(self.players.items()):
            p["budget"] = 120.0
            p["ipl_team"] = franchises[i % len(franchises)]
            p["secret_captain"] = captain_names[i % len(captain_names)]
            
            if p.get("ws"):
                import asyncio
                asyncio.create_task(p["ws"].send_json({
                    "type": "secret_mission",
                    "ipl_team": p["ipl_team"],
                    "secret_captain": p["secret_captain"]
                }))
            
        budgets_data = {}
        for uid, p in self.players.items():
            budgets_data[uid] = {
                "name": p["name"],
                "budget": p["budget"],
                "players": 0,
                "overseas": 0,
                "ipl_team": p.get("ipl_team", "Unknown")
            }"""

code = re.sub(
    r'''        for uid, p in self.players\.items\(\):
            p\["budget"\] = 120\.0
            
        budgets_data = \{\}
        for uid, p in self\.players\.items\(\):
            budgets_data\[uid\] = \{
                "name": p\["name"\],
                "budget": p\["budget"\],
                "players": 0,
                "overseas": 0
            \}''',
    start_patch,
    code
)

# 2. Update sync_player_state and sell_player budget_data dicts
code = code.replace(
    '"overseas": sum(1 for pl in team if pl.get("nationality", "").lower() != "indian")',
    '"overseas": sum(1 for pl in team if pl.get("nationality", "").lower() != "indian"),\n                    "ipl_team": p.get("ipl_team", "Unknown")'
)

code = code.replace(
    '"overseas": sum(1 for pl in uid_team if pl.get("nationality", "").lower() != "indian")',
    '"overseas": sum(1 for pl in uid_team if pl.get("nationality", "").lower() != "indian"),\n                        "ipl_team": p.get("ipl_team", "Unknown")'
)

# Also in sync_player_state we need to send the secret mission again!
sync_patch = """                await player_info["ws"].send_json({
                    "type": "auction_start",
                    "total_players": len(self.cricket_players),
                    "budgets": budgets_data
                })
                
                # Resend secret mission
                if "secret_captain" in player_info:
                    await player_info["ws"].send_json({
                        "type": "secret_mission",
                        "ipl_team": player_info.get("ipl_team"),
                        "secret_captain": player_info.get("secret_captain")
                    })"""

code = code.replace(
    """                await player_info["ws"].send_json({
                    "type": "auction_start",
                    "total_players": len(self.cricket_players),
                    "budgets": budgets_data
                })""",
    sync_patch
)

# 3. Update end_auction to pass secret_captain
code = code.replace(
    'score = self.calculate_team_scores(team, player_info["budget"])',
    'score = self.calculate_team_scores(team, player_info["budget"], player_info.get("secret_captain"))'
)

# 4. Update calculate_team_scores signature and logic
code = code.replace(
    'def calculate_team_scores(self, team: List[dict], remaining_budget: float) -> float:',
    'def calculate_team_scores(self, team: List[dict], remaining_budget: float, secret_captain: str = None) -> float:'
)

calc_patch = """        # Format cleanly out of 10
        final_score = round(max(0.0, min(10.0, score / 10.0)), 1)
        
        # Secret Captain Bonus (Can break the 10.0 limit!)
        if secret_captain:
            for p in team:
                if p["name"] == secret_captain:
                    final_score += 0.5
                    break
                    
        return final_score"""

code = code.replace(
    """        # Format cleanly out of 10
        final_score = round(max(0.0, min(10.0, score / 10.0)), 1)
        return final_score""",
    calc_patch
)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Backend patched")
