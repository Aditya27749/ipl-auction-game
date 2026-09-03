import sqlite3

superstars3 = {
    "Jos Buttler": {"matches": 107, "runs": 3582, "wickets": 0, "batting_avg": 38.0, "strike_rate": 147.5},
    "Sai Sudharsan": {"matches": 25, "runs": 1034, "wickets": 0, "batting_avg": 47.0, "strike_rate": 139.1},
    "Jofra Archer": {"matches": 40, "runs": 195, "wickets": 48, "batting_avg": 15.0, "strike_rate": 157.2},
    "Mitchell Starc": {"matches": 41, "runs": 116, "wickets": 51, "batting_avg": 13.0, "strike_rate": 106.0},
    "Sam Curran": {"matches": 59, "runs": 883, "wickets": 58, "batting_avg": 22.0, "strike_rate": 133.0},
    "Manish Pandey": {"matches": 171, "runs": 3850, "wickets": 0, "batting_avg": 29.0, "strike_rate": 121.5},
    "Suryakumar Yadav": {"matches": 150, "runs": 3594, "wickets": 0, "batting_avg": 32.3, "strike_rate": 145.3},
    "Tom Curran": {"matches": 13, "runs": 127, "wickets": 13, "batting_avg": 18.0, "strike_rate": 115.0}
}

conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
for name, stats in superstars3.items():
    cursor.execute("""
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    """, (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], name))
conn.commit()
conn.close()

# Update apply_cricsheet_stats.py
with open("apply_cricsheet_stats.py", "a") as f:
    f.write("\nsuperstars3 = {\n")
    for name, stats in superstars3.items():
        f.write(f'    "{name}": {stats},\n')
    f.write("}\n\n")
    f.write("""conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
for name, stats in superstars3.items():
    cursor.execute(\"\"\"
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    \"\"\", (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], name))
conn.commit()
conn.close()
""")

print("Fixed batch 3.")
