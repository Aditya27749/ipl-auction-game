import sqlite3
import random

extra_players = [
    # Domestic & Past Indian Players
    ("Aakash Chopra", "Indian", "Batsman", "None"),
    ("Abhinav Mukund", "Indian", "Batsman", "None"),
    ("Abhishek Nayar", "Indian", "All-Rounder", "Medium"),
    ("Aditya Tare", "Indian", "Wicket-Keeper", "None"),
    ("Ajit Agarkar", "Indian", "Bowler", "Fast-Medium"),
    ("Akshdeep Nath", "Indian", "Batsman", "Medium"),
    ("Ankit Sharma", "Indian", "All-Rounder", "Slow Left-arm"),
    ("Anureet Singh", "Indian", "Bowler", "Fast-Medium"),
    ("Ashish Nehra", "Indian", "Bowler", "Fast-Medium"),
    ("Ashok Dinda", "Indian", "Bowler", "Fast-Medium"),
    ("Baba Aparajith", "Indian", "All-Rounder", "Off-break"),
    ("Baba Indrajith", "Indian", "Wicket-Keeper", "None"),
    ("Baltej Singh", "Indian", "Bowler", "Fast-Medium"),
    ("Barinder Sran", "Indian", "Bowler", "Fast-Medium"),
    ("Basil Thampi", "Indian", "Bowler", "Fast-Medium"),
    ("Bipul Sharma", "Indian", "All-Rounder", "Slow Left-arm"),
    ("Chama Milind", "Indian", "Bowler", "Fast-Medium"),
    ("CM Gautam", "Indian", "Wicket-Keeper", "None"),
    ("Dhawal Kulkarni", "Indian", "Bowler", "Fast-Medium"),
    ("Gurkeerat Singh Mann", "Indian", "All-Rounder", "Off-break"),
    ("Hanuma Vihari", "Indian", "Batsman", "Off-break"),
    ("Iqbal Abdulla", "Indian", "All-Rounder", "Slow Left-arm"),
    ("Irfan Pathan", "Indian", "All-Rounder", "Fast-Medium"),
    ("Jalaj Saxena", "Indian", "All-Rounder", "Off-break"),
    ("Joginder Sharma", "Indian", "All-Rounder", "Fast-Medium"),
    ("Manan Vohra", "Indian", "Batsman", "None"),
    ("Mandeep Singh", "Indian", "Batsman", "Medium"),
    ("Manpreet Gony", "Indian", "Bowler", "Fast-Medium"),
    ("Mayank Agarwal", "Indian", "Batsman", "None"),
    ("Manoj Tiwary", "Indian", "Batsman", "Leg-break"),
    ("Milind Kumar", "Indian", "Batsman", "Off-break"),
    ("Mohammad Kaif", "Indian", "Batsman", "None"),
    ("Munaf Patel", "Indian", "Bowler", "Fast-Medium"),
    ("Murugan Ashwin", "Indian", "Bowler", "Leg-break"),
    ("Nathu Singh", "Indian", "Bowler", "Fast-Medium"),
    ("Parthiv Patel", "Indian", "Wicket-Keeper", "None"),
    ("Paul Valthaty", "Indian", "All-Rounder", "Medium"),
    ("Pawan Negi", "Indian", "All-Rounder", "Slow Left-arm"),
    ("Pragyan Ojha", "Indian", "Bowler", "Slow Left-arm"),
    ("Praveen Kumar", "Indian", "Bowler", "Fast-Medium"),
    ("Pravin Tambe", "Indian", "Bowler", "Leg-break"),
    ("Rajat Bhatia", "Indian", "All-Rounder", "Medium"),
    ("Ramesh Powar", "Indian", "Bowler", "Off-break"),
    ("RP Singh", "Indian", "Bowler", "Fast-Medium"),
    ("Rishi Dhawan", "Indian", "All-Rounder", "Fast-Medium"),
    ("Sachin Baby", "Indian", "Batsman", "Off-break"),
    ("Sandeep Warrier", "Indian", "Bowler", "Fast-Medium"),
    ("Saurabh Tiwary", "Indian", "Batsman", "None"),
    ("Shahbaz Nadeem", "Indian", "Bowler", "Slow Left-arm"),
    ("Sreesanth", "Indian", "Bowler", "Fast-Medium"),
    ("Stuart Binny", "Indian", "All-Rounder", "Fast-Medium"),
    ("Swapnil Singh", "Indian", "All-Rounder", "Slow Left-arm"),
    ("Unmukt Chand", "Indian", "Batsman", "None"),
    ("Varun Aaron", "Indian", "Bowler", "Fast"),
    ("Vijay Shankar", "Indian", "All-Rounder", "Medium"),
    ("Vinay Kumar", "Indian", "Bowler", "Fast-Medium"),
    ("Wasim Jaffer", "Indian", "Batsman", "None"),
    ("Yusuf Pathan", "Indian", "All-Rounder", "Off-break"),
    ("Anukul Roy", "Indian", "All-Rounder", "Slow Left-arm"),
    ("Atharva Taide", "Indian", "Batsman", "None"),
    
    # Overseas Past/Present Players
    ("Ajantha Mendis", "Overseas", "Bowler", "Spin"),
    ("Albie Morkel", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Andrew Tye", "Overseas", "Bowler", "Fast-Medium"),
    ("Angelo Mathews", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Ben Cutting", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Brad Hodge", "Overseas", "Batsman", "Off-break"),
    ("Brad Hogg", "Overseas", "Bowler", "Spin"),
    ("Carlos Brathwaite", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Chris Lynn", "Overseas", "Batsman", "None"),
    ("Colin de Grandhomme", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Corey Anderson", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Daniel Christian", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Daniel Vettori", "Overseas", "Bowler", "Slow Left-arm"),
    ("Darren Sammy", "Overseas", "All-Rounder", "Fast-Medium"),
    ("David Hussey", "Overseas", "All-Rounder", "Off-break"),
    ("Dirk Nannes", "Overseas", "Bowler", "Fast"),
    ("Doug Bollinger", "Overseas", "Bowler", "Fast-Medium"),
    ("Dwayne Bravo", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Dwayne Smith", "Overseas", "All-Rounder", "Medium"),
    ("Evin Lewis", "Overseas", "Batsman", "None"),
    ("George Bailey", "Overseas", "Batsman", "None"),
    ("Hashim Amla", "Overseas", "Batsman", "None"),
    ("Herschelle Gibbs", "Overseas", "Batsman", "None"),
    ("Imran Tahir", "Overseas", "Bowler", "Leg-break"),
    ("James Faulkner", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Jason Behrendorff", "Overseas", "Bowler", "Fast-Medium"),
    ("Kevon Cooper", "Overseas", "All-Rounder", "Medium"),
    ("Lendl Simmons", "Overseas", "Batsman", "Medium"),
    ("Mahela Jayawardene", "Overseas", "Batsman", "None"),
    ("Marlon Samuels", "Overseas", "All-Rounder", "Off-break"),
    ("Mitchell Johnson", "Overseas", "Bowler", "Fast"),
    ("Mitchell McClenaghan", "Overseas", "Bowler", "Fast-Medium"),
    ("Moises Henriques", "Overseas", "All-Rounder", "Fast-Medium"),
    ("Morne Morkel", "Overseas", "Bowler", "Fast"),
    ("Nathan Coulter-Nile", "Overseas", "Bowler", "Fast-Medium"),
    ("Ross Taylor", "Overseas", "Batsman", "None"),
    ("Ryan ten Doeschate", "Overseas", "All-Rounder", "Medium"),
    ("Scott Styris", "Overseas", "All-Rounder", "Medium"),
    ("Sean Abbott", "Overseas", "Bowler", "Fast-Medium"),
    ("Shaun Tait", "Overseas", "Bowler", "Fast"),
    ("Sheldon Cottrell", "Overseas", "Bowler", "Fast-Medium"),
    ("Tymal Mills", "Overseas", "Bowler", "Fast")
]

teams = ["CSK", "RCB", "MI", "KKR", "SRH", "RR", "DC", "PBKS", "LSG", "GT", "Unsold"]

def generate_stats_and_insert():
    conn = sqlite3.connect('ipl_auction.db')
    cursor = conn.cursor()
    
    added = 0
    for player in extra_players:
        name, nationality, role, bowling_style = player
        
        matches = random.randint(15, 120)
        ipl_team = random.choice(teams)
        
        if role == 'Batsman' or role == 'Wicket-Keeper':
            runs = random.randint(300, 3500)
            wickets = 0
            batting_avg = round(random.uniform(22.0, 36.0), 2)
            bowling_avg = 0.0
            sr = round(random.uniform(120.0, 155.0), 2)
            economy = 0.0
            base_price = random.choice([0.5, 1.0, 1.5, 2.0])
            rating = round(random.uniform(7.0, 8.8), 1)
            
        elif role == 'Bowler':
            runs = random.randint(10, 300)
            wickets = random.randint(20, 120)
            batting_avg = round(random.uniform(5.0, 12.0), 2)
            bowling_avg = round(random.uniform(19.0, 30.0), 2)
            sr = round(random.uniform(85.0, 125.0), 2)
            economy = round(random.uniform(6.5, 9.0), 2)
            base_price = random.choice([0.5, 1.0, 1.5, 2.0])
            rating = round(random.uniform(7.0, 8.8), 1)
            
        else: # All-Rounder
            runs = random.randint(400, 2000)
            wickets = random.randint(25, 90)
            batting_avg = round(random.uniform(18.0, 30.0), 2)
            bowling_avg = round(random.uniform(21.0, 32.0), 2)
            sr = round(random.uniform(125.0, 160.0), 2)
            economy = round(random.uniform(7.2, 8.8), 2)
            base_price = random.choice([0.5, 1.0, 1.5, 2.0])
            rating = round(random.uniform(7.5, 8.9), 1)
            
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
    print(f"Successfully added {added} historical/extra players to the database!")

if __name__ == "__main__":
    generate_stats_and_insert()
