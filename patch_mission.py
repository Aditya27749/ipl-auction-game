import re

with open("game_engine.py", "r") as f:
    code = f.read()

target = """        # Secret Captain Bonus (Can break the 10.0 limit!)
        bonus = 0.0
        if secret_captain:
            for p in team:
                if p["name"] == secret_captain:
                    bonus = 0.5
                    final_score += bonus
                    break
                    
        return {"""

replace = """        # Secret Captain Bonus/Penalty (Can break the 10.0 limit!)
        bonus = 0.0
        mission_status = "N/A"
        if secret_captain:
            found = False
            for p in team:
                if p["name"] == secret_captain:
                    found = True
                    break
            
            if found:
                bonus = 0.5
                final_score += bonus
                mission_status = "Success"
            else:
                bonus = -0.5
                final_score += bonus
                mission_status = "Failed"
                    
        return {
            "secret_captain": secret_captain,
            "mission_status": mission_status,"""

code = code.replace(target, replace)

with open("game_engine.py", "w") as f:
    f.write(code)

print("game_engine.py mission patched")
