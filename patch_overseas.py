import re

with open("game_engine.py", "r") as f:
    code = f.read()

target1 = """        structure_score = 25 - (bat_penalty + bwl_penalty + ar_penalty + wk_penalty)
        score += max(0, structure_score)
        
        # Penalty for empty squad slots (Must be 15)
        missing_players = 15 - len(team)
        score -= (missing_players * 3)

        # 2. Overseas Limits (Max 5 Points)
        if overseas_count <= 6:
            score += 5
        else:
            score -= (overseas_count - 6) * 5"""

replace1 = """        structure_score = 30 - (bat_penalty + bwl_penalty + ar_penalty + wk_penalty)
        score += max(0, structure_score)
        
        # Penalty for empty squad slots (Must be 15)
        missing_players = 15 - len(team)
        score -= (missing_players * 3)

        # 2. Overseas Limits (Penalty Only)
        overseas_penalty = 0.0
        if overseas_count > 6:
            overseas_penalty = -((overseas_count - 6) * 5)
            score += overseas_penalty"""

code = code.replace(target1, replace1)

target2 = """        # Breakdown values scaled to /10
        structure_display = round(max(0.0, structure_score / 10.0), 2)
        overseas_display = 0.5 if overseas_count <= 6 else round(max(0.0, (5 - (overseas_count - 6) * 5) / 10.0), 2)"""

replace2 = """        # Breakdown values scaled to /10
        structure_display = round(max(0.0, structure_score / 10.0), 2)
        overseas_penalty_display = round(overseas_penalty / 10.0, 2)"""

code = code.replace(target2, replace2)

target3 = """            "structure": structure_display,
            "overseas": overseas_display,"""

replace3 = """            "structure": structure_display,
            "overseas_penalty": overseas_penalty_display,"""

code = code.replace(target3, replace3)

with open("game_engine.py", "w") as f:
    f.write(code)

print("game_engine.py patched.")
