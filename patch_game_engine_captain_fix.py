import re
with open("game_engine.py", "r") as f:
    code = f.read()

target = """        # Reset budgets and UI
        for p in self.players.values():
            p["budget"] = 120.0
            
        budgets_data = {uid: 120.0 for uid in self.players.keys()}"""

replacement = """        # Assign teams and secret captains
        franchises = ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Rajasthan Royals", "Sunrisers Hyderabad", "Delhi Capitals", "Punjab Kings", "Gujarat Titans", "Lucknow Super Giants"]
        import random
        random.shuffle(franchises)
        
        # We need ALL players to get top ones
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

code = code.replace(target, replacement)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Fixed start_auction.")
