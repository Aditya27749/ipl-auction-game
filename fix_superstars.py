import sqlite3

superstars = {
    "Rohit Sharma": {"matches": 257, "runs": 6628, "wickets": 15, "batting_avg": 29.72, "strike_rate": 131.14},
    "Suryakumar Yadav": {"matches": 150, "runs": 3594, "wickets": 0, "batting_avg": 32.37, "strike_rate": 145.3},
    "Hardik Pandya": {"matches": 137, "runs": 2525, "wickets": 64, "batting_avg": 28.5, "strike_rate": 146.0},
    "Rishabh Pant": {"matches": 111, "runs": 3284, "wickets": 0, "batting_avg": 35.31, "strike_rate": 148.93},
    "Shreyas Iyer": {"matches": 115, "runs": 3127, "wickets": 0, "batting_avg": 32.24, "strike_rate": 127.42},
    "Jasprit Bumrah": {"matches": 133, "runs": 69, "wickets": 165, "batting_avg": 0, "strike_rate": 0},
    "Ravindra Jadeja": {"matches": 240, "runs": 2959, "wickets": 160, "batting_avg": 27.4, "strike_rate": 129.0},
    "KL Rahul": {"matches": 132, "runs": 4683, "wickets": 0, "batting_avg": 45.0, "strike_rate": 134.4},
    "Sanju Samson": {"matches": 167, "runs": 4419, "wickets": 0, "batting_avg": 30.6, "strike_rate": 139.0},
    "Yuzvendra Chahal": {"matches": 160, "runs": 43, "wickets": 205, "batting_avg": 0, "strike_rate": 0},
    "MS Dhoni": {"matches": 264, "runs": 5243, "wickets": 0, "batting_avg": 39.12, "strike_rate": 137.5},
    "Virat Kohli": {"matches": 252, "runs": 8004, "wickets": 4, "batting_avg": 38.6, "strike_rate": 131.9},
    "Andre Russell": {"matches": 127, "runs": 2484, "wickets": 115, "batting_avg": 29.5, "strike_rate": 174.0},
    "Sunil Narine": {"matches": 176, "runs": 1534, "wickets": 180, "batting_avg": 17.0, "strike_rate": 165.8}
}

conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()

for name, stats in superstars.items():
    cursor.execute("""
        UPDATE players 
        SET matches=?, runs=?, wickets=?, batting_avg=?, strike_rate=?
        WHERE name=?
    """, (stats["matches"], stats["runs"], stats["wickets"], stats["batting_avg"], stats["strike_rate"], name))

conn.commit()
conn.close()
print("Superstars fixed.")
