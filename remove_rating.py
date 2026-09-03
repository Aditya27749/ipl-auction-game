with open("game_engine.py", "r") as f:
    code = f.read()

import re

# Update Runs to 35
code = code.replace(
    "runs_points = min(25.0, (total_runs / expected_championship_runs) * 25.0)",
    "runs_points = min(35.0, (total_runs / expected_championship_runs) * 35.0)"
)

# Update Wickets to 35
code = code.replace(
    "wickets_points = min(25.0, (total_wickets / expected_championship_wickets) * 25.0)",
    "wickets_points = min(35.0, (total_wickets / expected_championship_wickets) * 35.0)"
)

# Delete rating logic
rating_logic = """        # 4. Star Power & Rating Synergy (Max 20 Points)
        # Captures intangible factors (strike rate aura, captaincy, etc.)
        avg_rating = total_rating / len(team)
        rating_points = (avg_rating / 10.0) * 20.0
        score += rating_points"""

code = code.replace(rating_logic, "")

with open("game_engine.py", "w") as f:
    f.write(code)
