import sqlite3
import random

names = ["Kumar Kushagra", "Sameer Rizvi", "Abhinav Manohar", "Sai Sudharsan", "Lalit Yadav", "Aman Khan", "Pravin Dubey", "Yash Dhull", "Priyam Garg", "Anmolpreet Singh", "Vivrant Sharma", "Mayank Dagar", "Sanvir Singh", "Harpreet Singh Bhatia", "Shashank Singh", "Prerak Mankad", "Vicky Ostwal", "Abishek Porel", "Ricky Bhui", "Swastik Chikara", "Saurav Chauhan", "Avanish Rao Aravelly", "Luvnith Sisodia", "Aryan Juyal", "Bipin Saurabh", "BR Sharath", "Urvil Patel", "Vishnu Vinod", "Harvik Desai", "G Ajitesh", "Gourav Choudhary", "Bipin Saurabh", "Fazalhaq Farooqi", "Noor Ahmad", "Naveen-ul-Haq", "Mujeeb Ur Rahman"]
conn = sqlite3.connect('ipl_auction.db')
cursor = conn.cursor()
added = 0
for name in names:
    try:
        cursor.execute("INSERT INTO players (name, nationality, role, bowling_style, ipl_team, matches, runs, wickets, batting_avg, bowling_avg, strike_rate, economy, base_price, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, "Indian", "Batsman", "None", "Unsold", 10, 200, 0, 25.0, 0.0, 130.0, 0.0, 0.5, 7.5))
        added += 1
    except sqlite3.IntegrityError:
        pass
conn.commit()
conn.close()
print(f"Added {added} more players")
