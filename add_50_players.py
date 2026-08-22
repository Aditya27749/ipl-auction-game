import sqlite3
import random

new_players = [
    # Promising Indian Players
    ("Nehal Wadhera", "Indian", "Batsman", "None"),
    ("Tilak Varma", "Indian", "Batsman", "Off-break"),
    ("Ayush Badoni", "Indian", "Batsman", "Off-break"),
    ("Mohsin Khan", "Indian", "Bowler", "Fast-Medium"),
    ("Yash Thakur", "Indian", "Bowler", "Fast-Medium"),
    ("Ramandeep Singh", "Indian", "All-Rounder", "Fast-Medium"),
    ("Harshit Rana", "Indian", "Bowler", "Fast"),
    ("Vaibhav Arora", "Indian", "Bowler", "Fast-Medium"),
    ("Suyash Prabhudessai", "Indian", "Batsman", "None"),
    ("Akash Deep", "Indian", "Bowler", "Fast-Medium"),
    ("Mukesh Kumar", "Indian", "Bowler", "Fast-Medium"),
    ("Kumar Kartikeya", "Indian", "Bowler", "Slow Left-arm"),
    ("Hrithik Shokeen", "Indian", "All-Rounder", "Off-break"),
    ("Arjun Tendulkar", "Indian", "Bowler", "Fast-Medium"),
    ("Arshad Khan", "Indian", "All-Rounder", "Fast-Medium"),
    ("Dhruv Jurel", "Indian", "Wicket-Keeper", "None"),
    ("Sai Sudharsan", "Indian", "Batsman", "None"),
    ("Shahrukh Khan", "Indian", "All-Rounder", "Off-break"),
    ("R. Sai Kishore", "Indian", "Bowler", "Slow Left-arm"),
    ("Yash Dhull", "Indian", "Batsman", "None"),
    ("Raj Angad Bawa", "Indian", "All-Rounder", "Fast-Medium"),
    ("Angkrish Raghuvanshi", "Indian", "Batsman", "None"),
    ("Naman Dhir", "Indian", "All-Rounder", "Off-break"),
    ("Shivalik Sharma", "Indian", "Batsman", "None"),
    ("Nitish Kumar Reddy", "Indian", "All-Rounder", "Fast-Medium"),
    ("Mayank Dagar", "Indian", "Bowler", "Slow Left-arm"),
    ("Vidwath Kaverappa", "Indian", "Bowler", "Fast-Medium"),
    ("Rasikh Salam", "Indian", "Bowler", "Fast-Medium"),
    ("Darshan Nalkande", "Indian", "Bowler", "Fast-Medium"),
    ("Prabhsimran Singh", "Indian", "Wicket-Keeper", "None"),
    ("Jitesh Sharma", "Indian", "Wicket-Keeper", "None"), # Added back just in case
    
    # International Stars & Emerging Players
    ("Spencer Johnson", "Overseas", "Bowler", "Fast"),
    ("Gerald Coetzee", "Overseas", "Bowler", "Fast"),
    ("Kwena Maphaka", "Overseas", "Bowler", "Fast"),
    ("Luke Wood", "Overseas", "Bowler", "Fast-Medium"),
    ("Shamar Joseph", "Overseas", "Bowler", "Fast"),
    ("Phil Salt", "Overseas", "Wicket-Keeper", "None"),
    ("Will Jacks", "Overseas", "All-Rounder", "Off-break"),
    ("Cameron Green", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Aaron Hardie", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Matt Short", "Overseas", "All-Rounder", "Off-break"),
    ("Josh Inglis", "Overseas", "Wicket-Keeper", "None"),
    ("Riley Meredith", "Overseas", "Bowler", "Fast"),
    ("Lance Morris", "Overseas", "Bowler", "Fast"),
    ("Nathan Ellis", "Overseas", "Bowler", "Fast-Medium"),
    ("Jhye Richardson", "Overseas", "Bowler", "Fast"),
    ("Kyle Jamieson", "Overseas", "Bowler", "Fast-Medium"),
    ("Adam Zampa", "Overseas", "Bowler", "Leg-break"),
    ("Ashton Agar", "Overseas", "All-Rounder", "Slow Left-arm"),
    ("Michael Bracewell", "Overseas", "All-Rounder", "Off-break"),
    ("Rachin Ravindra", "Overseas", "All-Rounder", "Slow Left-arm")
]

teams = ["CSK", "RCB", "MI", "KKR", "SRH", "RR", "DC", "PBKS", "LSG", "GT", "Unsold"]

def generate_stats_and_insert():
    conn = sqlite3.connect('ipl_auction.db')
    cursor = conn.cursor()
    
    added = 0
    for player in new_players:
        name, nationality, role, bowling_style = player
        
        # Generate realistic random stats based on role
        matches = random.randint(5, 60)
        ipl_team = random.choice(teams)
        
        if role == 'Batsman' or role == 'Wicket-Keeper':
            runs = random.randint(300, 2000)
            wickets = 0
            batting_avg = round(random.uniform(20.0, 38.0), 2)
            bowling_avg = 0.0
            sr = round(random.uniform(130.0, 165.0), 2)
            economy = 0.0
            base_price = random.choice([0.5, 1.0, 1.5, 2.0])
            rating = round(random.uniform(7.0, 8.4), 1)
            
        elif role == 'Bowler':
            runs = random.randint(10, 250)
            wickets = random.randint(10, 80)
            batting_avg = round(random.uniform(5.0, 15.0), 2)
            bowling_avg = round(random.uniform(18.0, 32.0), 2)
            sr = round(random.uniform(90.0, 120.0), 2)
            economy = round(random.uniform(7.0, 9.5), 2)
            base_price = random.choice([0.5, 1.0, 1.5, 2.0])
            rating = round(random.uniform(7.0, 8.3), 1)
            
        else: # All-Rounder
            runs = random.randint(200, 1200)
            wickets = random.randint(15, 60)
            batting_avg = round(random.uniform(15.0, 28.0), 2)
            bowling_avg = round(random.uniform(22.0, 35.0), 2)
            sr = round(random.uniform(125.0, 155.0), 2)
            economy = round(random.uniform(7.5, 9.0), 2)
            base_price = random.choice([0.5, 1.0, 1.5, 2.0])
            rating = round(random.uniform(7.5, 8.6), 1)
            
        # Exceptions for specific stars
        if name in ["Cameron Green", "Phil Salt", "Rachin Ravindra", "Tilak Varma"]:
            rating = round(random.uniform(8.5, 8.8), 1)
            base_price = 2.0
            
        try:
            cursor.execute('''
                INSERT INTO players 
                (name, nationality, role, bowling_style, ipl_team, matches, runs, wickets, batting_avg, bowling_avg, strike_rate, economy, base_price, rating)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, nationality, role, bowling_style, ipl_team, matches, runs, wickets, batting_avg, bowling_avg, sr, economy, base_price, rating))
            added += 1
        except sqlite3.IntegrityError:
            pass
            
    conn.commit()
    conn.close()
    print(f"Successfully added {added} new players to the database!")

if __name__ == "__main__":
    generate_stats_and_insert()
