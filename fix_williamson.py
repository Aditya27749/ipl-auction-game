import sqlite3

stats = {
    "matches": 77,
    "runs": 2101,
    "wickets": 0,
    "batting_avg": 36.2,
    "strike_rate": 126.0,
    "role": "Batsman"
}

# Update DB
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
cursor.execute("""
    UPDATE players 
    SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?, role=?
    WHERE name='Kane Williamson'
""", (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], stats["role"]))
conn.commit()
conn.close()

# Update apply_cricsheet_stats.py
append_code = """
# Fix Kane Williamson
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
cursor.execute(\"\"\"
    UPDATE players 
    SET matches=77, runs=2101, wickets=0, batting_avg=36.2, strike_rate=126.0, role='Batsman'
    WHERE name='Kane Williamson'
\"\"\")
conn.commit()
conn.close()
"""
with open("apply_cricsheet_stats.py", "a") as f:
    f.write(append_code)

print("Fixed Kane Williamson.")
