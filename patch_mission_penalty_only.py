import re

with open("game_engine.py", "r") as f:
    code = f.read()

target = """        # Secret Captain Bonus/Penalty (Can break the 10.0 limit!)
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
                mission_status = "Failed" """

replace = """        # Secret Captain Penalty Only (No bonus points allowed)
        bonus = 0.0
        mission_status = "N/A"
        if secret_captain:
            found = False
            for p in team:
                if p["name"] == secret_captain:
                    found = True
                    break
            
            if found:
                bonus = 0.0
                mission_status = "Success"
            else:
                bonus = -0.5
                final_score += bonus
                mission_status = "Failed" """

code = code.replace(target, replace)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Mission penalty only patched.")
