import re

with open("game_engine.py", "r") as f:
    code = f.read()

old_list = 'franchises = ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Rajasthan Royals", "Sunrisers Hyderabad", "Delhi Capitals", "Punjab Kings", "Gujarat Titans", "Lucknow Super Giants"]'
new_list = 'franchises = ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders", "Rajasthan Royals", "Sunrisers Hyderabad", "Delhi Capitals", "Punjab Kings", "Gujarat Titans", "Lucknow Super Giants", "Deccan Chargers", "Pune Warriors India", "Kochi Tuskers Kerala", "Gujarat Lions", "Rising Pune Supergiant", "Sydney Sixers", "Perth Scorchers", "Trinbago Knight Riders", "Barbados Royals", "MI Cape Town"]'

code = code.replace(old_list, new_list)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Franchises expanded.")
