import sqlite3

rahane_stats = {
    "name": "Ajinkya Rahane",
    "nationality": "Indian",
    "role": "Batsman",
    "bowling_style": "None",
    "ipl_team": "CSK",
    "matches": 185,
    "runs": 4642,
    "wickets": 1,
    "batting_avg": 30.2,
    "bowling_avg": 5.0,
    "strike_rate": 123.4,
    "economy": 5.0,
    "base_price": 1.5,
    "rating": 8.5
}

# Update local DB
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()

# Check if exists
cursor.execute("SELECT id FROM players WHERE name = ?", (rahane_stats["name"],))
exists = cursor.fetchone()

if not exists:
    cursor.execute("""
        INSERT INTO players (name, nationality, role, bowling_style, ipl_team, matches, runs, wickets, batting_avg, bowling_avg, strike_rate, economy, base_price, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (rahane_stats["name"], rahane_stats["nationality"], rahane_stats["role"], rahane_stats["bowling_style"], rahane_stats["ipl_team"], 
          rahane_stats["matches"], rahane_stats["runs"], rahane_stats["wickets"], rahane_stats["batting_avg"], rahane_stats["bowling_avg"], 
          rahane_stats["strike_rate"], rahane_stats["economy"], rahane_stats["base_price"], rahane_stats["rating"]))
else:
    cursor.execute("""
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    """, (rahane_stats["matches"], rahane_stats["runs"], rahane_stats["wickets"], rahane_stats["batting_avg"], rahane_stats["strike_rate"], rahane_stats["name"]))

conn.commit()
conn.close()

# Append to apply_cricsheet_stats.py
append_code = """
# Add Ajinkya Rahane (missing from initial seed)
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
cursor.execute("SELECT id FROM players WHERE name = 'Ajinkya Rahane'")
if not cursor.fetchone():
    cursor.execute(\"\"\"
        INSERT INTO players (name, nationality, role, bowling_style, ipl_team, matches, runs, wickets, batting_avg, bowling_avg, strike_rate, economy, base_price, rating)
        VALUES ('Ajinkya Rahane', 'Indian', 'Batsman', 'None', 'CSK', 185, 4642, 1, 30.2, 5.0, 123.4, 5.0, 1.5, 8.5)
    \"\"\")
else:
    cursor.execute(\"\"\"
        UPDATE players 
        SET matches=185, runs=4642, wickets=1, batting_avg=30.2, strike_rate=123.4
        WHERE name='Ajinkya Rahane'
    \"\"\")
conn.commit()
conn.close()
"""

with open("apply_cricsheet_stats.py", "a") as f:
    f.write(append_code)

print("Added Rahane.")
