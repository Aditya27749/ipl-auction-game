import sqlite3

# Update DB
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
cursor.execute("UPDATE players SET rating=10.0 WHERE name IN ('Virat Kohli', 'Jasprit Bumrah', 'Andre Russell', 'MS Dhoni');")
conn.commit()
conn.close()

# Update apply_cricsheet_stats.py
append_code = """
# Create the 4 God-Tier 10.0 Rated Players
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
cursor.execute("UPDATE players SET rating=10.0 WHERE name IN ('Virat Kohli', 'Jasprit Bumrah', 'Andre Russell', 'MS Dhoni');")
conn.commit()
conn.close()
"""
with open("apply_cricsheet_stats.py", "a") as f:
    f.write(append_code)

print("Gods created.")
