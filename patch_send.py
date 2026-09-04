import re
with open("game_engine.py", "r") as f:
    code = f.read()

bad = """            if p.get("ws"):
                import asyncio
                asyncio.create_task(p["ws"].send_json({
                    "type": "secret_mission",
                    "ipl_team": p["ipl_team"],
                    "secret_captain": p["secret_captain"]
                }))"""

good = """            if p.get("ws"):
                await p["ws"].send_json({
                    "type": "secret_mission",
                    "ipl_team": p["ipl_team"],
                    "secret_captain": p["secret_captain"]
                })"""

code = code.replace(bad, good)
with open("game_engine.py", "w") as f:
    f.write(code)
