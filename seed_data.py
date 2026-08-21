import sqlite3

def seed_players(db_path='ipl_auction.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            nationality TEXT,
            role TEXT,
            bowling_style TEXT,
            ipl_team TEXT,
            matches INTEGER,
            runs INTEGER,
            wickets INTEGER,
            batting_avg REAL,
            bowling_avg REAL,
            strike_rate REAL,
            economy REAL,
            base_price REAL,
            rating REAL
        )
    ''')

    players = [
        # Marquee Batsmen (rating 8-10)
        ("Virat Kohli", "Indian", "Batsman", None, "RCB", 250, 8000, 4, 38.0, 90.5, 132.0, 8.5, 2.0, 9.5),
        ("Rohit Sharma", "Indian", "Batsman", "Spin", "MI", 250, 6500, 15, 30.0, 45.0, 130.0, 8.0, 2.0, 9.0),
        ("Shubman Gill", "Indian", "Batsman", None, "GT", 80, 2800, 0, 36.0, 0.0, 132.0, 0.0, 2.0, 8.5),
        ("KL Rahul", "Indian", "Wicket-Keeper", None, "LSG", 120, 4600, 0, 45.0, 0.0, 134.0, 0.0, 2.0, 8.5),
        ("Suryakumar Yadav", "Indian", "Batsman", "Medium", "MI", 100, 2800, 0, 32.0, 0.0, 150.0, 0.0, 2.0, 8.5),
        ("Faf du Plessis", "Overseas", "Batsman", "Spin", "RCB", 120, 3800, 0, 34.0, 0.0, 135.0, 0.0, 1.5, 8.0),
        ("David Warner", "Overseas", "Batsman", None, "DC", 180, 6500, 0, 42.0, 0.0, 140.0, 0.0, 1.5, 8.0),
        ("Jos Buttler", "Overseas", "Wicket-Keeper", None, "RR", 90, 3200, 0, 38.0, 0.0, 150.0, 0.0, 2.0, 8.5),
        ("Quinton de Kock", "Overseas", "Wicket-Keeper", None, "LSG", 100, 3000, 0, 32.0, 0.0, 138.0, 0.0, 1.5, 8.0),
        ("Travis Head", "Overseas", "Batsman", "Spin", "SRH", 20, 600, 2, 35.0, 45.0, 165.0, 9.5, 1.5, 8.0),

        # Marquee Bowlers (rating 8-10)
        ("Jasprit Bumrah", "Indian", "Bowler", "Fast", "MI", 130, 80, 170, 8.0, 24.0, 100.0, 7.4, 2.0, 9.5),
        ("Mohammed Shami", "Indian", "Bowler", "Fast", "GT", 100, 95, 110, 9.5, 25.0, 95.0, 8.0, 1.5, 8.5),
        ("Rashid Khan", "Overseas", "Bowler", "Spin", "GT", 110, 450, 130, 15.0, 20.0, 145.0, 6.5, 2.0, 9.0),
        ("Yuzvendra Chahal", "Indian", "Bowler", "Spin", "RR", 150, 35, 190, 5.0, 22.0, 60.0, 7.5, 1.5, 8.5),
        ("Trent Boult", "Overseas", "Bowler", "Fast", "RR", 80, 40, 100, 6.0, 25.0, 75.0, 8.0, 1.5, 8.0),
        ("Kagiso Rabada", "Overseas", "Bowler", "Fast", "PBKS", 60, 120, 80, 12.0, 22.0, 110.0, 8.2, 1.5, 8.5),
        ("Mohammed Siraj", "Indian", "Bowler", "Fast", "RCB", 70, 50, 80, 6.0, 27.0, 80.0, 8.5, 1.0, 7.5),
        ("Arshdeep Singh", "Indian", "Bowler", "Fast", "PBKS", 50, 20, 60, 4.0, 26.0, 65.0, 8.8, 1.0, 7.5),

        # All-Rounders (rating 7-9)
        ("Hardik Pandya", "Indian", "All-Rounder", "Fast", "MI", 120, 2200, 55, 28.0, 32.0, 148.0, 8.5, 2.0, 8.5),
        ("Ravindra Jadeja", "Indian", "All-Rounder", "Spin", "CSK", 230, 2700, 160, 28.0, 30.0, 132.0, 7.6, 2.0, 9.0),
        ("Andre Russell", "Overseas", "All-Rounder", "Fast", "KKR", 110, 2200, 90, 28.0, 25.0, 175.0, 9.0, 2.0, 8.5),
        ("Glenn Maxwell", "Overseas", "All-Rounder", "Spin", "RCB", 110, 2500, 30, 25.0, 35.0, 155.0, 8.0, 2.0, 8.0),
        ("Marcus Stoinis", "Overseas", "All-Rounder", "Fast", "LSG", 60, 1300, 20, 28.0, 30.0, 142.0, 9.0, 1.5, 7.5),
        ("Sam Curran", "Overseas", "All-Rounder", "Fast", "PBKS", 40, 500, 40, 24.0, 28.0, 135.0, 8.5, 1.5, 8.0),
        ("Axar Patel", "Indian", "All-Rounder", "Spin", "DC", 90, 1200, 70, 22.0, 29.0, 140.0, 7.0, 1.5, 7.5),
        ("Shardul Thakur", "Indian", "All-Rounder", "Fast", "CSK", 80, 400, 65, 15.0, 28.0, 130.0, 8.8, 1.0, 7.0),

        # Wicket-Keepers (rating 6-8.5)
        ("MS Dhoni", "Indian", "Wicket-Keeper", None, "CSK", 270, 5200, 0, 39.0, 0.0, 136.0, 0.0, 2.0, 9.0),
        ("Rishabh Pant", "Indian", "Wicket-Keeper", None, "DC", 110, 3500, 0, 35.0, 0.0, 148.0, 0.0, 2.0, 8.5),
        ("Sanju Samson", "Indian", "Wicket-Keeper", None, "RR", 160, 4200, 0, 29.0, 0.0, 138.0, 0.0, 1.5, 7.5),
        ("Ishan Kishan", "Indian", "Wicket-Keeper", None, "MI", 80, 2300, 0, 28.0, 0.0, 136.0, 0.0, 1.0, 7.0),
        ("Dinesh Karthik", "Indian", "Wicket-Keeper", None, "RCB", 250, 4800, 0, 26.0, 0.0, 138.0, 0.0, 0.75, 7.0),
        ("Heinrich Klaasen", "Overseas", "Wicket-Keeper", None, "SRH", 25, 800, 0, 35.0, 0.0, 172.0, 0.0, 1.5, 8.0),

        # Mid-Tier Players (rating 5-7.5) - Batsmen
        ("Devdutt Padikkal", "Indian", "Batsman", None, "LSG", 55, 1500, 0, 28.0, 0.0, 125.0, 0.0, 0.5, 6.5),
        ("Ruturaj Gaikwad", "Indian", "Batsman", None, "CSK", 60, 2000, 0, 38.0, 0.0, 135.0, 0.0, 1.0, 7.5),
        ("Yashasvi Jaiswal", "Indian", "Batsman", "Spin", "RR", 45, 1400, 0, 32.0, 0.0, 150.0, 0.0, 1.0, 7.5),
        ("Prithvi Shaw", "Indian", "Batsman", None, "DC", 75, 1800, 0, 24.0, 0.0, 145.0, 0.0, 0.5, 6.0),
        ("Abhishek Sharma", "Indian", "Batsman", "Spin", "SRH", 50, 1200, 10, 26.0, 35.0, 155.0, 8.5, 0.5, 7.0),
        ("Tilak Varma", "Indian", "Batsman", "Spin", "MI", 35, 1100, 2, 38.0, 40.0, 145.0, 8.0, 0.5, 7.5),
        ("Sai Sudharsan", "Indian", "Batsman", "Spin", "GT", 25, 900, 0, 45.0, 0.0, 135.0, 0.0, 0.5, 7.0),
        ("Rinku Singh", "Indian", "Batsman", "Spin", "KKR", 40, 950, 0, 35.0, 0.0, 145.0, 0.0, 0.5, 7.5),
        ("Rahul Tripathi", "Indian", "Batsman", "Medium", "SRH", 95, 2200, 0, 27.0, 0.0, 138.0, 0.0, 0.75, 6.5),
        ("Nitish Rana", "Indian", "Batsman", "Spin", "KKR", 105, 2600, 10, 28.0, 32.0, 135.0, 8.2, 0.75, 6.5),
        
        # Mid-Tier Players (rating 5-7.5) - Bowlers
        ("Kuldeep Yadav", "Indian", "Bowler", "Spin", "DC", 75, 150, 85, 12.0, 26.0, 90.0, 7.8, 1.0, 7.5),
        ("Ravichandran Ashwin", "Indian", "Bowler", "Spin", "RR", 200, 750, 175, 13.0, 29.0, 115.0, 7.0, 1.5, 7.5),
        ("Bhuvneshwar Kumar", "Indian", "Bowler", "Fast", "SRH", 160, 300, 170, 10.0, 26.0, 100.0, 7.5, 1.5, 7.5),
        ("Umran Malik", "Indian", "Bowler", "Fast", "SRH", 25, 20, 30, 5.0, 28.0, 60.0, 9.2, 0.5, 6.5),
        ("Avesh Khan", "Indian", "Bowler", "Fast", "RR", 50, 40, 60, 6.0, 26.0, 75.0, 8.5, 0.5, 6.5),
        ("Harshal Patel", "Indian", "Bowler", "Fast", "PBKS", 90, 250, 115, 12.0, 24.0, 120.0, 8.5, 1.0, 7.0),
        ("Mohit Sharma", "Indian", "Bowler", "Fast", "GT", 100, 150, 120, 8.0, 23.0, 105.0, 8.2, 0.5, 7.0),
        ("Tushar Deshpande", "Indian", "Bowler", "Fast", "CSK", 25, 25, 25, 6.0, 28.0, 90.0, 9.5, 0.2, 6.0),
        ("Sandeep Sharma", "Indian", "Bowler", "Fast", "RR", 115, 100, 130, 7.0, 26.0, 85.0, 7.8, 0.5, 7.0),
        ("Mukesh Kumar", "Indian", "Bowler", "Fast", "DC", 15, 10, 12, 4.0, 32.0, 70.0, 9.8, 0.5, 5.5),
        ("Pat Cummins", "Overseas", "Bowler", "Fast", "SRH", 50, 400, 55, 18.0, 30.0, 150.0, 8.5, 2.0, 8.0),
        ("Mitchell Starc", "Overseas", "Bowler", "Fast", "KKR", 30, 100, 35, 12.0, 21.0, 110.0, 7.5, 2.0, 8.0),
        ("Josh Hazlewood", "Overseas", "Bowler", "Fast", "RCB", 30, 25, 38, 5.0, 22.0, 75.0, 8.0, 1.5, 7.5),
        ("Mustafizur Rahman", "Overseas", "Bowler", "Fast", "CSK", 55, 30, 58, 4.0, 28.0, 60.0, 8.0, 1.0, 7.0),
        ("Anrich Nortje", "Overseas", "Bowler", "Fast", "DC", 45, 50, 55, 7.0, 25.0, 85.0, 8.5, 1.0, 7.5),
        ("Marco Jansen", "Overseas", "Bowler", "Fast", "SRH", 20, 150, 20, 15.0, 32.0, 130.0, 9.2, 0.5, 6.5),
        ("Adam Zampa", "Overseas", "Bowler", "Spin", "RR", 20, 15, 30, 5.0, 20.0, 60.0, 7.8, 1.0, 7.0),

        # Mid-Tier Players (rating 5-7.5) - All-Rounders
        ("Sunil Narine", "Overseas", "All-Rounder", "Spin", "KKR", 170, 1500, 175, 16.0, 25.0, 165.0, 6.8, 1.5, 8.0),
        ("Venkatesh Iyer", "Indian", "All-Rounder", "Medium", "KKR", 40, 1100, 3, 30.0, 45.0, 135.0, 8.5, 0.5, 7.0),
        ("Washington Sundar", "Indian", "All-Rounder", "Spin", "SRH", 60, 400, 38, 14.0, 32.0, 120.0, 7.5, 1.0, 6.5),
        ("Krunal Pandya", "Indian", "All-Rounder", "Spin", "LSG", 115, 1500, 75, 22.0, 34.0, 130.0, 7.5, 1.0, 7.0),
        ("Liam Livingstone", "Overseas", "All-Rounder", "Spin", "PBKS", 35, 900, 10, 28.0, 38.0, 160.0, 9.0, 1.5, 7.5),
        ("Cameron Green", "Overseas", "All-Rounder", "Fast", "RCB", 20, 500, 10, 35.0, 35.0, 155.0, 9.5, 2.0, 7.5),
        ("Mitchell Marsh", "Overseas", "All-Rounder", "Medium", "DC", 40, 700, 38, 22.0, 22.0, 130.0, 8.2, 1.5, 7.5),
        ("Phil Salt", "Overseas", "Wicket-Keeper", None, "KKR", 15, 400, 0, 30.0, 0.0, 150.0, 0.0, 1.0, 7.0),

        # Budget Players (rating 3-5)
        ("Abhinav Manohar", "Indian", "Batsman", None, "GT", 15, 250, 0, 18.0, 0.0, 140.0, 0.0, 0.2, 4.5),
        ("Ayush Badoni", "Indian", "Batsman", "Spin", "LSG", 30, 450, 2, 22.0, 40.0, 130.0, 8.5, 0.2, 5.0),
        ("Prabhsimran Singh", "Indian", "Wicket-Keeper", None, "PBKS", 25, 500, 0, 20.0, 0.0, 145.0, 0.0, 0.2, 5.0),
        ("Dhruv Jurel", "Indian", "Wicket-Keeper", None, "RR", 15, 200, 0, 22.0, 0.0, 160.0, 0.0, 0.2, 5.0),
        ("Nehal Wadhera", "Indian", "Batsman", "Spin", "MI", 15, 250, 0, 25.0, 0.0, 145.0, 0.0, 0.2, 4.5),
        ("Yash Thakur", "Indian", "Bowler", "Fast", "LSG", 15, 10, 18, 5.0, 28.0, 80.0, 9.0, 0.2, 4.5),
        ("Akash Madhwal", "Indian", "Bowler", "Fast", "MI", 10, 5, 15, 3.0, 22.0, 60.0, 8.5, 0.2, 4.5),
        ("Vaibhav Arora", "Indian", "Bowler", "Fast", "KKR", 15, 15, 15, 5.0, 30.0, 70.0, 9.2, 0.2, 4.0),
        ("Harshit Rana", "Indian", "Bowler", "Fast", "KKR", 10, 20, 12, 6.0, 25.0, 85.0, 8.8, 0.2, 4.5),
        ("Suyash Sharma", "Indian", "Bowler", "Spin", "KKR", 12, 5, 10, 2.0, 32.0, 50.0, 8.5, 0.2, 4.5),
        ("Mayank Dagar", "Indian", "All-Rounder", "Spin", "RCB", 10, 50, 5, 12.0, 35.0, 110.0, 8.2, 0.2, 4.0),
        ("Ramandeep Singh", "Indian", "All-Rounder", "Medium", "KKR", 12, 150, 6, 18.0, 30.0, 140.0, 9.0, 0.2, 4.0),
        ("Vivrant Sharma", "Indian", "All-Rounder", "Spin", "SRH", 5, 80, 2, 25.0, 35.0, 120.0, 8.5, 0.2, 3.5),
        ("Hrithik Shokeen", "Indian", "Bowler", "Spin", "MI", 10, 40, 5, 10.0, 40.0, 100.0, 8.5, 0.2, 3.5),
        ("Kartik Tyagi", "Indian", "Bowler", "Fast", "GT", 20, 15, 15, 4.0, 35.0, 70.0, 9.5, 0.2, 4.0),
        
        # New Additions
        ("AB de Villiers", "Overseas", "Batsman", "Medium", "RCB", 184, 5162, 0, 39.7, 0.0, 151.68, 0.0, 2.0, 9.8),
        ("Chris Gayle", "Overseas", "Batsman", "Spin", "PBKS", 142, 4965, 18, 39.72, 34.0, 148.96, 7.9, 2.0, 9.5),
        ("Lasith Malinga", "Overseas", "Bowler", "Fast", "MI", 122, 88, 170, 5.5, 19.8, 95.0, 7.14, 2.0, 9.6),
        ("Suresh Raina", "Indian", "Batsman", "Spin", "CSK", 205, 5528, 25, 32.5, 34.0, 136.7, 7.3, 2.0, 9.0),
        ("Kieron Pollard", "Overseas", "All-Rounder", "Medium", "MI", 189, 3412, 69, 28.67, 31.6, 147.32, 8.7, 2.0, 8.8),
        ("Shikhar Dhawan", "Indian", "Batsman", "Spin", "PBKS", 217, 6617, 4, 35.38, 16.5, 127.14, 8.2, 1.5, 8.5),
        ("Gautam Gambhir", "Indian", "Batsman", "Spin", "KKR", 154, 4217, 0, 31.0, 0.0, 123.88, 0.0, 1.5, 8.0),
        ("Shane Watson", "Overseas", "All-Rounder", "Medium", "CSK", 145, 3874, 92, 30.99, 29.15, 137.91, 7.93, 1.5, 8.5),
        ("Sachin Tendulkar", "Indian", "Batsman", "Spin", "MI", 78, 2334, 0, 34.83, 0.0, 119.81, 0.0, 2.0, 9.0),
        ("Yuvraj Singh", "Indian", "All-Rounder", "Spin", "PBKS", 132, 2750, 36, 24.77, 29.91, 129.71, 7.43, 2.0, 8.5),
        
        # Even More Additions (Current Stars)
        ("Shreyas Iyer", "Indian", "Batsman", "Spin", "KKR", 115, 3127, 0, 32.23, 0.0, 127.42, 0.0, 1.5, 8.0),
        ("Shivam Dube", "Indian", "All-Rounder", "Medium", "CSK", 65, 1378, 4, 30.62, 34.25, 148.97, 9.13, 1.0, 8.0),
        ("Jofra Archer", "Overseas", "Bowler", "Fast", "MI", 40, 195, 48, 15.0, 24.39, 157.25, 7.43, 2.0, 8.5),
        ("Nicholas Pooran", "Overseas", "Wicket-Keeper", None, "LSG", 75, 1769, 0, 31.03, 0.0, 159.22, 0.0, 2.0, 8.5),
        ("Tim David", "Overseas", "Batsman", "Medium", "MI", 38, 659, 0, 28.65, 0.0, 172.51, 0.0, 1.5, 7.5),
        ("Matheesha Pathirana", "Overseas", "Bowler", "Fast", "CSK", 20, 0, 34, 0.0, 17.52, 0.0, 7.87, 1.0, 8.5),
        ("Rajat Patidar", "Indian", "Batsman", "Spin", "RCB", 27, 799, 0, 34.73, 0.0, 158.53, 0.0, 0.5, 7.5),
        ("Rachin Ravindra", "Overseas", "All-Rounder", "Spin", "CSK", 14, 222, 0, 15.85, 0.0, 160.86, 0.0, 1.0, 7.0),
        ("Tristan Stubbs", "Overseas", "Wicket-Keeper", None, "DC", 18, 405, 0, 45.0, 0.0, 176.08, 0.0, 1.0, 8.0),
        ("Gerald Coetzee", "Overseas", "Bowler", "Fast", "MI", 10, 14, 13, 7.0, 26.23, 116.66, 10.18, 1.0, 7.5),
        ("Mayank Yadav", "Indian", "Bowler", "Fast", "LSG", 3, 0, 7, 0.0, 12.14, 0.0, 6.98, 0.2, 7.5),
        ("Jake Fraser-McGurk", "Overseas", "Batsman", "Spin", "DC", 9, 330, 0, 36.66, 0.0, 234.04, 0.0, 0.5, 8.0)
    ]

    for p in players:
        try:
            cursor.execute('''
                INSERT INTO players (
                    name, nationality, role, bowling_style, ipl_team, 
                    matches, runs, wickets, batting_avg, bowling_avg, 
                    strike_rate, economy, base_price, rating
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', p)
        except sqlite3.IntegrityError:
            pass # Skip if player already exists (name is UNIQUE)

    conn.commit()
    print(f"Successfully seeded {len(players)} players into {db_path} (duplicates ignored)")
    conn.close()

if __name__ == '__main__':
    seed_players()
