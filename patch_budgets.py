with open("game_engine.py", "r") as f:
    code = f.read()

import re

# Patch sync_player_state
code = re.sub(
    r'budgets_data = \{uid: \{"name": p\["name"\], "budget": p\["budget"\]\} for uid, p in self.players.items()\}',
    r'''budgets_data = {}
            for uid, p in self.players.items():
                team = get_drafted_players(self.room_id, uid)
                budgets_data[uid] = {
                    "name": p["name"],
                    "budget": p["budget"],
                    "players": len(team),
                    "overseas": sum(1 for pl in team if pl.get("nationality", "").lower() != "indian")
                }''',
    code
)

# Patch start_auction
code = re.sub(
    r'budgets_data = \{uid: 120.0 for uid in self.players.keys()\}',
    r'''budgets_data = {}
        for uid, p in self.players.items():
            budgets_data[uid] = {
                "name": p["name"],
                "budget": p["budget"],
                "players": 0,
                "overseas": 0
            }''',
    code
)

# Patch sell_player
code = re.sub(
    r'''                budgets_data = \{\}
                for uid, p in self.players.items\(\):
                    budgets_data\[uid\] = \{"name": p\["name"\], "budget": p\["budget"\]\}''',
    r'''                budgets_data = {}
                for uid, p in self.players.items():
                    uid_team = get_drafted_players(self.room_id, uid)
                    budgets_data[uid] = {
                        "name": p["name"], 
                        "budget": p["budget"],
                        "players": len(uid_team),
                        "overseas": sum(1 for pl in uid_team if pl.get("nationality", "").lower() != "indian")
                    }''',
    code
)

with open("game_engine.py", "w") as f:
    f.write(code)
