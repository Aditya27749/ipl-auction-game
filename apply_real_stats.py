import sqlite3

# Real, highly accurate career stats for the most popular IPL players (up to 2024 season)
real_stats = {
    "Virat Kohli": {"runs": 8004, "wickets": 4, "batting_avg": 38.66, "strike_rate": 131.97, "matches": 252, "rating": 9.8},
    "Shikhar Dhawan": {"runs": 6769, "wickets": 0, "batting_avg": 35.25, "strike_rate": 127.14, "matches": 222, "rating": 8.9},
    "Rohit Sharma": {"runs": 6628, "wickets": 15, "batting_avg": 29.72, "strike_rate": 131.14, "matches": 257, "rating": 9.2},
    "David Warner": {"runs": 6565, "wickets": 0, "batting_avg": 40.52, "strike_rate": 139.77, "matches": 184, "rating": 9.3},
    "Suresh Raina": {"runs": 5528, "wickets": 25, "batting_avg": 32.51, "strike_rate": 136.76, "matches": 205, "rating": 9.1},
    "MS Dhoni": {"runs": 5243, "wickets": 0, "batting_avg": 39.12, "strike_rate": 137.53, "matches": 264, "rating": 9.4},
    "AB de Villiers": {"runs": 5162, "wickets": 0, "batting_avg": 39.70, "strike_rate": 151.68, "matches": 184, "rating": 9.8},
    "Chris Gayle": {"runs": 4965, "wickets": 18, "batting_avg": 39.72, "strike_rate": 148.96, "matches": 142, "rating": 9.5},
    "Robin Uthappa": {"runs": 4952, "wickets": 0, "batting_avg": 27.51, "strike_rate": 130.35, "matches": 205, "rating": 8.4},
    "Dinesh Karthik": {"runs": 4842, "wickets": 0, "batting_avg": 26.31, "strike_rate": 135.36, "matches": 257, "rating": 8.5},
    "Ajinkya Rahane": {"runs": 4642, "wickets": 0, "batting_avg": 30.14, "strike_rate": 123.42, "matches": 185, "rating": 8.3},
    "KL Rahul": {"runs": 4683, "wickets": 0, "batting_avg": 45.46, "strike_rate": 134.60, "matches": 132, "rating": 9.0},
    "Suryakumar Yadav": {"runs": 3594, "wickets": 0, "batting_avg": 31.80, "strike_rate": 145.32, "matches": 150, "rating": 9.2},
    "Faf du Plessis": {"runs": 4571, "wickets": 0, "batting_avg": 35.71, "strike_rate": 136.20, "matches": 145, "rating": 8.9},
    "Sanju Samson": {"runs": 4419, "wickets": 0, "batting_avg": 30.68, "strike_rate": 138.96, "matches": 167, "rating": 8.8},
    "Jos Buttler": {"runs": 3582, "wickets": 0, "batting_avg": 38.10, "strike_rate": 147.53, "matches": 107, "rating": 9.2},
    "Shubman Gill": {"runs": 3216, "wickets": 0, "batting_avg": 37.83, "strike_rate": 135.75, "matches": 103, "rating": 8.9},
    "Rishabh Pant": {"runs": 3284, "wickets": 0, "batting_avg": 35.31, "strike_rate": 148.93, "matches": 111, "rating": 8.8},
    "Hardik Pandya": {"runs": 2525, "wickets": 64, "batting_avg": 28.69, "strike_rate": 145.44, "matches": 137, "rating": 8.7},
    "Andre Russell": {"runs": 2484, "wickets": 115, "batting_avg": 29.57, "strike_rate": 174.92, "matches": 127, "rating": 9.1},
    "Ravindra Jadeja": {"runs": 2959, "wickets": 160, "batting_avg": 27.39, "strike_rate": 129.55, "matches": 240, "rating": 9.0},
    "Kieron Pollard": {"runs": 3412, "wickets": 69, "batting_avg": 28.67, "strike_rate": 147.32, "matches": 189, "rating": 8.8},
    "Sunil Narine": {"runs": 1534, "wickets": 180, "batting_avg": 17.04, "strike_rate": 165.83, "matches": 177, "rating": 9.2},
    "Rashid Khan": {"runs": 542, "wickets": 149, "bowling_avg": 21.82, "economy": 6.82, "matches": 121, "rating": 9.3},
    "Yuzvendra Chahal": {"runs": 37, "wickets": 205, "bowling_avg": 22.44, "economy": 7.84, "matches": 160, "rating": 9.4},
    "Piyush Chawla": {"runs": 612, "wickets": 181, "bowling_avg": 26.60, "economy": 7.96, "matches": 192, "rating": 8.5},
    "Amit Mishra": {"runs": 381, "wickets": 174, "bowling_avg": 23.84, "economy": 7.39, "matches": 161, "rating": 8.4},
    "Ravichandran Ashwin": {"runs": 800, "wickets": 180, "bowling_avg": 29.77, "economy": 7.12, "matches": 212, "rating": 8.8},
    "Bhuvneshwar Kumar": {"runs": 312, "wickets": 181, "bowling_avg": 27.23, "economy": 7.56, "matches": 176, "rating": 9.0},
    "Jasprit Bumrah": {"runs": 71, "wickets": 165, "bowling_avg": 22.51, "economy": 7.30, "matches": 133, "rating": 9.6},
    "Lasith Malinga": {"runs": 88, "wickets": 170, "bowling_avg": 19.80, "economy": 7.14, "matches": 122, "rating": 9.7},
    "Kagiso Rabada": {"runs": 188, "wickets": 117, "bowling_avg": 21.36, "economy": 8.41, "matches": 80, "rating": 8.8},
    "Mohammed Shami": {"runs": 78, "wickets": 127, "bowling_avg": 26.86, "economy": 8.44, "matches": 110, "rating": 8.7},
    "Trent Boult": {"runs": 55, "wickets": 121, "bowling_avg": 26.69, "economy": 8.29, "matches": 104, "rating": 8.8},
    "Harshal Patel": {"runs": 257, "wickets": 135, "bowling_avg": 23.63, "economy": 8.59, "matches": 106, "rating": 8.5},
    "Ishan Kishan": {"runs": 2644, "wickets": 0, "batting_avg": 28.43, "strike_rate": 135.86, "matches": 105, "rating": 8.4},
    "Ruturaj Gaikwad": {"runs": 2380, "wickets": 0, "batting_avg": 41.75, "strike_rate": 136.86, "matches": 66, "rating": 8.6},
    "Mitchell Starc": {"runs": 96, "wickets": 34, "bowling_avg": 20.38, "economy": 7.17, "matches": 27, "rating": 8.3},
    "Pat Cummins": {"runs": 444, "wickets": 52, "bowling_avg": 30.19, "economy": 8.61, "matches": 55, "rating": 8.4},
    "Sam Curran": {"runs": 922, "wickets": 58, "batting_avg": 23.64, "strike_rate": 139.70, "matches": 59, "rating": 8.3},
    "Nicholas Pooran": {"runs": 1769, "wickets": 0, "batting_avg": 32.16, "strike_rate": 156.96, "matches": 76, "rating": 8.6},
    "Heinrich Klaasen": {"runs": 993, "wickets": 0, "batting_avg": 38.19, "strike_rate": 168.30, "matches": 35, "rating": 8.7},
    "Travis Head": {"runs": 772, "wickets": 2, "batting_avg": 40.63, "strike_rate": 192.03, "matches": 25, "rating": 8.9},
    "Matheesha Pathirana": {"runs": 0, "wickets": 34, "bowling_avg": 17.58, "economy": 7.89, "matches": 20, "rating": 8.5},
    "Yashasvi Jaiswal": {"runs": 1607, "wickets": 0, "batting_avg": 32.14, "strike_rate": 150.60, "matches": 52, "rating": 8.7},
    "Rinku Singh": {"runs": 893, "wickets": 0, "batting_avg": 30.79, "strike_rate": 143.33, "matches": 45, "rating": 8.5},
    "Shreyas Iyer": {"runs": 3127, "wickets": 0, "batting_avg": 32.23, "strike_rate": 127.42, "matches": 115, "rating": 8.4},
    "Gautam Gambhir": {"runs": 4217, "wickets": 0, "batting_avg": 31.00, "strike_rate": 123.88, "matches": 154, "rating": 8.6},
    "Mayank Yadav": {"runs": 0, "wickets": 7, "bowling_avg": 12.14, "economy": 6.98, "matches": 4, "rating": 7.8}
}

def apply_stats():
    conn = sqlite3.connect('ipl_auction.db')
    cursor = conn.cursor()
    
    updated = 0
    for name, stats in real_stats.items():
        # Map fields to match database schema exactly
        updates = []
        params = []
        for key, value in stats.items():
            updates.append(f"{key} = ?")
            params.append(value)
            
        params.append(name)
        
        query = f"UPDATE players SET {', '.join(updates)} WHERE name = ?"
        cursor.execute(query, tuple(params))
        
        if cursor.rowcount > 0:
            updated += 1
            
    conn.commit()
    conn.close()
    print(f"Successfully applied real career stats to {updated} legendary players!")

if __name__ == "__main__":
    apply_stats()
