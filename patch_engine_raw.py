import re

with open("game_engine.py", "r") as f:
    code = f.read()

target = """        return {
            "total": final_score,
            "structure": structure_display,
            "overseas": overseas_display,
            "runs": runs_display,
            "wickets": wickets_display,
            "sr_penalty": round(sr_penalty / 10.0, 1),
            "econ_penalty": round(econ_penalty / 10.0, 1),
            "bonus": bonus
        }"""

replace = """        return {
            "total": final_score,
            "structure": structure_display,
            "overseas": overseas_display,
            "runs": runs_display,
            "wickets": wickets_display,
            "sr_penalty": round(sr_penalty / 10.0, 1),
            "econ_penalty": round(econ_penalty / 10.0, 1),
            "bonus": bonus,
            "raw_runs": total_runs,
            "raw_wickets": total_wickets,
            "raw_sr": round(avg_sr, 2),
            "raw_econ": round(avg_econ, 2)
        }"""

code = code.replace(target, replace)

with open("game_engine.py", "w") as f:
    f.write(code)

print("game_engine.py raw stats patched")
