import sqlite3

superstars2 = {
    "Travis Head": {"matches": 30, "runs": 900, "wickets": 2, "batting_avg": 35.0, "strike_rate": 165.0},
    "Piyush Chawla": {"matches": 192, "runs": 613, "wickets": 192, "batting_avg": 11.5, "strike_rate": 111.4},
    "Imran Tahir": {"matches": 59, "runs": 20, "wickets": 82, "batting_avg": 10.0, "strike_rate": 80.0},
    "Munaf Patel": {"matches": 63, "runs": 39, "wickets": 74, "batting_avg": 7.8, "strike_rate": 85.0},
    "Colin Munro": {"matches": 13, "runs": 177, "wickets": 0, "batting_avg": 14.7, "strike_rate": 125.5},
    "Chris Lynn": {"matches": 42, "runs": 1329, "wickets": 0, "batting_avg": 34.0, "strike_rate": 140.6},
    "Martin Guptill": {"matches": 13, "runs": 270, "wickets": 0, "batting_avg": 22.5, "strike_rate": 137.7}
}

# Update the DB
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
for name, stats in superstars2.items():
    cursor.execute("""
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    """, (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], name))
conn.commit()
conn.close()

# Update apply_cricsheet_stats.py
with open("apply_cricsheet_stats.py", "r") as f:
    content = f.read()

# Generate the dict code to append
append_code = "\nsuperstars2 = {\n"
for name, stats in superstars2.items():
    append_code += f'    "{name}": {stats},\n'
append_code += "}\n\n"
append_code += """conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
for name, stats in superstars2.items():
    cursor.execute(\"\"\"
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    \"\"\", (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], name))
conn.commit()
conn.close()
"""

with open("apply_cricsheet_stats.py", "a") as f:
    f.write(append_code)

print("Fixed players.")
