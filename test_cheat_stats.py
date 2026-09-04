import sqlite3

cheat_names = [
    "Shikhar Dhawan", "David Warner", "Suresh Raina", "Gautam Gambhir", "Shubman Gill",
    "Shane Watson", "Jacques Kallis", "Abhishek Nayar",
    "Bhuvneshwar Kumar", "Yuzvendra Chahal", "Ravichandran Ashwin", "Amit Mishra", "Sandeep Sharma",
    "Dinesh Karthik", "Aditya Tare"
]

conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()

total_sr = 0
batters = 0

total_econ = 0
bowlers = 0

for name in cheat_names:
    cursor.execute("SELECT role, strike_rate, economy FROM players WHERE name=?", (name,))
    row = cursor.fetchone()
    if row:
        role, sr, econ = row
        if role in ['Batsman', 'Wicket-Keeper', 'All-Rounder'] and sr > 0:
            total_sr += sr
            batters += 1
            
        if role in ['Bowler', 'All-Rounder'] and econ > 0:
            total_econ += econ
            bowlers += 1

print(f"Avg SR: {total_sr/batters if batters else 0:.2f}")
print(f"Avg Econ: {total_econ/bowlers if bowlers else 0:.2f}")

conn.close()
