import sqlite3

# List of legendary IPL players to add
new_legends = [
    ("Adam Gilchrist", "Overseas", "Wicket-Keeper", "None", "Deccan Chargers", 80, 2069, 0, 27.22, 0, 138.39, 0, 2.0, 9.2),
    ("Virender Sehwag", "Indian", "Batsman", "None", "Delhi Daredevils", 104, 2728, 6, 27.55, 35.83, 155.44, 8.5, 2.0, 9.3),
    ("Yuvraj Singh", "Indian", "All-Rounder", "Slow Left-arm", "Punjab Kings", 132, 2750, 36, 24.77, 29.91, 129.71, 7.43, 2.0, 9.1),
    ("Shane Watson", "Overseas", "All-Rounder", "Fast-Medium", "Rajasthan Royals", 145, 3874, 92, 30.99, 29.15, 137.91, 7.93, 2.0, 9.5),
    ("Zaheer Khan", "Indian", "Bowler", "Fast-Medium", "Mumbai Indians", 100, 117, 102, 11.7, 27.27, 84.7, 7.58, 2.0, 9.0),
    ("Muttiah Muralitharan", "Overseas", "Bowler", "Off-break", "Chennai Super Kings", 66, 24, 63, 6.0, 26.92, 85.0, 6.67, 2.0, 9.2),
    ("Dale Steyn", "Overseas", "Bowler", "Fast", "Sunrisers Hyderabad", 95, 166, 97, 8.3, 25.85, 102.4, 6.91, 2.0, 9.4),
    ("Michael Hussey", "Overseas", "Batsman", "None", "Chennai Super Kings", 59, 1977, 0, 38.76, 0, 122.64, 0, 2.0, 8.9),
    ("Jacques Kallis", "Overseas", "All-Rounder", "Fast-Medium", "Kolkata Knight Riders", 98, 2427, 65, 28.55, 35.27, 109.22, 7.89, 2.0, 9.1),
    ("Brendon McCullum", "Overseas", "Wicket-Keeper", "None", "Kolkata Knight Riders", 109, 2880, 0, 27.69, 0, 131.74, 0, 2.0, 9.0),
    ("Harbhajan Singh", "Indian", "Bowler", "Off-break", "Mumbai Indians", 163, 833, 150, 15.14, 26.86, 137.9, 7.05, 2.0, 9.0),
    ("Anil Kumble", "Indian", "Bowler", "Leg-break", "Royal Challengers Bangalore", 42, 35, 45, 11.6, 23.51, 78.5, 6.57, 2.0, 9.1),
    ("Matthew Hayden", "Overseas", "Batsman", "None", "Chennai Super Kings", 32, 1107, 0, 36.9, 0, 137.51, 0, 2.0, 8.9),
    ("Shaun Marsh", "Overseas", "Batsman", "None", "Punjab Kings", 71, 2477, 0, 39.95, 0, 132.74, 0, 2.0, 8.8),
    ("Chris Morris", "Overseas", "All-Rounder", "Fast-Medium", "Rajasthan Royals", 81, 618, 95, 15.84, 23.98, 155.27, 8.0, 2.0, 8.9)
]

def add_legends():
    conn = sqlite3.connect('ipl_auction.db')
    cursor = conn.cursor()
    
    added = 0
    for legend in new_legends:
        try:
            cursor.execute('''
                INSERT INTO players 
                (name, nationality, role, bowling_style, ipl_team, matches, runs, wickets, batting_avg, bowling_avg, strike_rate, economy, base_price, rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', legend)
            added += 1
        except sqlite3.IntegrityError:
            # Player already exists
            pass
            
    conn.commit()
    conn.close()
    print(f"Successfully added {added} historical legends!")

if __name__ == "__main__":
    add_legends()
