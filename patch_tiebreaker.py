import re

with open("game_engine.py", "r") as f:
    code = f.read()

target = """        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)"""

replace = """        # Sort by score descending, then tiebreaker: Total Runs, then Total Wickets
        results.sort(key=lambda x: (
            x["score"], 
            x.get("score_breakdown", {}).get("raw_runs", 0), 
            x.get("score_breakdown", {}).get("raw_wickets", 0)
        ), reverse=True)"""

code = code.replace(target, replace)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Tiebreaker patched.")
