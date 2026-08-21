import sqlite3
import random

db_path = 'ipl_auction.db'

names = [
    "Jason Roy", "Ben Stokes", "Joe Root", "Dawid Malan", "Eoin Morgan", 
    "Alex Hales", "Adil Rashid", "Mark Wood", "Chris Woakes", "Moeen Ali", 
    "Sam Billings", "Liam Plunkett", "Tom Curran", "Reece Topley", "Jason Holder", 
    "Akeal Hosein", "Rovman Powell", "Shimron Hetmyer", "Kyle Mayers", "Romario Shepherd", 
    "Alzarri Joseph", "Odean Smith", "Sherfane Rutherford", "Obed McCoy", "Rassie van der Dussen", 
    "David Miller", "Aiden Markram", "Dewald Brevis", "Lungi Ngidi", "Tabraiz Shamsi", 
    "Wayne Parnell", "Keshav Maharaj", "Duan Jansen", "Donovan Ferreira", "Nandre Burger", 
    "Kane Williamson", "Devon Conway", "Glenn Phillips", "Daryl Mitchell", "Mitchell Santner", 
    "Tim Southee", "Lockie Ferguson", "Matt Henry", "Ish Sodhi", "Colin Munro", 
    "Martin Guptill", "Rahmanullah Gurbaz", "Naveen-ul-Haq", "Fazalhaq Farooqi", "Noor Ahmad", 
    "Mujeeb Ur Rahman", "Mohammad Nabi", "Azmatullah Omarzai", "Gulbadin Naib", "Shakib Al Hasan", 
    "Taskin Ahmed", "Litton Das", "Shoriful Islam", "Wanindu Hasaranga", "Maheesh Theekshana", 
    "Dushmantha Chameera", "Dilshan Madushanka", "Nuwan Thushara", "Bhanuka Rajapaksa", "Dasun Shanaka", 
    "Kusal Mendis", "Charith Asalanka", "Manish Pandey", "Deepak Hooda", "Kedar Jadhav", 
    "Ambati Rayudu", "Robin Uthappa", "Piyush Chawla", "Amit Mishra", "Ishant Sharma", 
    "Umesh Yadav", "Jaydev Unadkat", "Siddarth Kaul", "Navdeep Saini", "Shivam Mavi", 
    "Kamlesh Nagarkoti", "Chetan Sakariya", "Khaleel Ahmed", "T Natarajan", "Shahbaz Ahmed", 
    "Rahul Tewatia", "Abdul Samad", "Mahipal Lomror", "Riyan Parag", "Shashank Singh", 
    "Ashutosh Sharma", "Jitesh Sharma", "Anuj Rawat", "Srikar Bharat", "Narayan Jagadeesan", 
    "Sheldon Jackson", "Upendra Yadav", "Vishnu Vinod", "Harpreet Brar", "Rahul Chahar", 
    "Ravi Bishnoi", "Mayank Markande", "Shreyas Gopal", "Karn Sharma", "Deepak Chahar", 
    "Sameer Rizvi", "Prerak Mankad", "Vicky Ostwal", "Abishek Porel", "Ricky Bhui", "Kumar Kushagra"
]

teams = ["CSK", "MI", "RCB", "KKR", "DC", "RR", "PBKS", "SRH", "LSG", "GT"]
roles = ["Batsman", "Bowler", "All-Rounder", "Wicket-Keeper"]
bowling_styles = ["Fast", "Spin", "Medium", None]

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

inserted_count = 0

for name in names:
    nationality = "Indian" if any(indian_name in name for indian_name in ["Pandey", "Hooda", "Jadhav", "Rayudu", "Uthappa", "Chawla", "Mishra", "Sharma", "Yadav", "Unadkat", "Kaul", "Saini", "Mavi", "Nagarkoti", "Sakariya", "Ahmed", "Natarajan", "Tewatia", "Samad", "Lomror", "Parag", "Singh", "Rawat", "Bharat", "Jagadeesan", "Jackson", "Vinod", "Brar", "Chahar", "Bishnoi", "Markande", "Gopal", "Rizvi", "Mankad", "Ostwal", "Porel", "Bhui", "Kushagra"]) else "Overseas"
    
    # Infer role roughly
    if name in ["Ben Stokes", "Moeen Ali", "Jason Holder", "Kyle Mayers", "Shakib Al Hasan", "Mohammad Nabi", "Azmatullah Omarzai", "Dasun Shanaka", "Rahul Tewatia", "Shahbaz Ahmed", "Mitchell Santner"]:
        role = "All-Rounder"
    elif name in ["Mark Wood", "Adil Rashid", "Lungi Ngidi", "Kagiso Rabada", "Trent Boult", "Tim Southee", "Lockie Ferguson", "Naveen-ul-Haq", "Rashid Khan", "Fazalhaq Farooqi", "Noor Ahmad", "Maheesh Theekshana", "Mustafizur Rahman", "Wanindu Hasaranga", "Piyush Chawla", "Amit Mishra", "Ishant Sharma", "Umesh Yadav", "T Natarajan", "Ravi Bishnoi", "Rahul Chahar", "Deepak Chahar"]:
        role = "Bowler"
    elif name in ["Sam Billings", "Quinton de Kock", "Rahmanullah Gurbaz", "Litton Das", "Kusal Mendis", "Jitesh Sharma", "Anuj Rawat", "Srikar Bharat", "Narayan Jagadeesan", "Abishek Porel"]:
        role = "Wicket-Keeper"
    else:
        role = random.choice(["Batsman", "Batsman", "Bowler", "All-Rounder"])
        
    team = random.choice(teams)
    
    if role == "Batsman":
        b_style = random.choice(["Spin", "Medium", None])
        matches = random.randint(10, 150)
        runs = random.randint(200, 4000)
        wickets = random.randint(0, 5)
        bat_avg = round(random.uniform(20.0, 45.0), 2)
        bow_avg = 0.0
        sr = round(random.uniform(120.0, 160.0), 2)
        eco = 0.0
        rating = round(random.uniform(5.5, 8.5), 1)
        base_price = random.choice([0.5, 1.0, 1.5, 2.0])
    elif role == "Bowler":
        b_style = random.choice(["Fast", "Spin"])
        matches = random.randint(10, 150)
        runs = random.randint(10, 500)
        wickets = random.randint(10, 150)
        bat_avg = round(random.uniform(5.0, 15.0), 2)
        bow_avg = round(random.uniform(18.0, 35.0), 2)
        sr = round(random.uniform(80.0, 130.0), 2)
        eco = round(random.uniform(6.5, 9.5), 2)
        rating = round(random.uniform(5.5, 8.5), 1)
        base_price = random.choice([0.5, 1.0, 1.5, 2.0])
    elif role == "All-Rounder":
        b_style = random.choice(["Fast", "Spin", "Medium"])
        matches = random.randint(10, 150)
        runs = random.randint(300, 2500)
        wickets = random.randint(10, 100)
        bat_avg = round(random.uniform(15.0, 35.0), 2)
        bow_avg = round(random.uniform(20.0, 35.0), 2)
        sr = round(random.uniform(125.0, 155.0), 2)
        eco = round(random.uniform(7.0, 9.0), 2)
        rating = round(random.uniform(6.5, 9.0), 1)
        base_price = random.choice([0.5, 1.0, 1.5, 2.0])
    else: # Wicket-Keeper
        b_style = None
        matches = random.randint(10, 150)
        runs = random.randint(200, 3500)
        wickets = 0
        bat_avg = round(random.uniform(20.0, 40.0), 2)
        bow_avg = 0.0
        sr = round(random.uniform(125.0, 160.0), 2)
        eco = 0.0
        rating = round(random.uniform(6.0, 8.5), 1)
        base_price = random.choice([0.5, 1.0, 1.5, 2.0])
        
    p = (name, nationality, role, b_style, team, matches, runs, wickets, bat_avg, bow_avg, sr, eco, base_price, rating)
    
    try:
        cursor.execute('''
            INSERT INTO players (
                name, nationality, role, bowling_style, ipl_team, 
                matches, runs, wickets, batting_avg, bowling_avg, 
                strike_rate, economy, base_price, rating
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', p)
        inserted_count += 1
    except sqlite3.IntegrityError:
        pass # Skip if exists

conn.commit()
print(f"Successfully added {inserted_count} new players to {db_path}!")
conn.close()
