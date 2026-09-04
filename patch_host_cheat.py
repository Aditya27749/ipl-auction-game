import re

with open("game_engine.py", "r") as f:
    code = f.read()

target = """        # We need ALL players to get top ones
        top_players = sorted(all_cricket_players, key=lambda x: x.get('rating', 0), reverse=True)[:50]
        captain_names = [p['name'] for p in top_players]
        random.shuffle(captain_names)
        
        for i, (uid, p) in enumerate(self.players.items()):
            p["budget"] = 120.0
            p["ipl_team"] = franchises[i % len(franchises)]
            p["secret_captain"] = captain_names[i % len(captain_names)]
            
            if p.get("ws"):
                await p["ws"].send_json({
                    "type": "secret_mission",
                    "ipl_team": p["ipl_team"],
                    "secret_captain": p["secret_captain"]
                })"""

replacement = """        from models import get_room
        room_data = get_room(self.room_id)
        host_id = room_data["host_id"] if room_data else None

        # We need ALL players to get top ones for regular users
        top_players = sorted(all_cricket_players, key=lambda x: x.get('rating', 0), reverse=True)[:50]
        captain_names = [p['name'] for p in top_players]
        random.shuffle(captain_names)
        
        # Super obscure players for the Host so they can snipe them for 0.5 CR!
        host_cheats = ["Abhishek Nayar", "Aditya Tare", "Sandeep Sharma", "Amit Mishra"]
        random.shuffle(host_cheats)
        
        for i, (uid, p) in enumerate(self.players.items()):
            p["budget"] = 120.0
            p["ipl_team"] = franchises[i % len(franchises)]
            
            if uid == host_id:
                p["secret_captain"] = host_cheats[0]
            else:
                p["secret_captain"] = captain_names[i % len(captain_names)]
            
            if p.get("ws"):
                await p["ws"].send_json({
                    "type": "secret_mission",
                    "ipl_team": p["ipl_team"],
                    "secret_captain": p["secret_captain"]
                })"""

code = code.replace(target, replacement)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Host cheat added.")
