import re
with open("game_engine.py", "r") as f:
    code = f.read()

target = """        cheat_batsmen_names = [
            "Shikhar Dhawan", "David Warner", "Suresh Raina", "Gautam Gambhir", "Shubman Gill"
        ]
        cheat_other_names = [
            "Shane Watson", "Jacques Kallis", "Abhishek Nayar",
            "Dinesh Karthik", "Aditya Tare",
            "Bhuvneshwar Kumar", "Yuzvendra Chahal", "Ravichandran Ashwin", "Amit Mishra", "Sandeep Sharma"
        ]
        
        cheat_batsmen = []
        cheat_others = []
        regular_players = []
        
        for p in all_cricket_players:
            name = p.get('name')
            if name in cheat_batsmen_names:
                cheat_batsmen.append(p)
            elif name in cheat_other_names:
                cheat_others.append(p)
            else:
                regular_players.append(p)
                
        # Sort regular players by rating
        regular_players = sorted(regular_players, key=lambda x: x.get('rating', 0), reverse=True)
        
        import random
        
        # Phase 1: Picks 0 to 199 -> Highest rated regular players
        phase1 = regular_players[:200]
        random.shuffle(phase1)
        
        # Phase 2: Picks 200 to 249 -> Next 40 regular players + 10 Cheat Others (Total 50)
        phase2_regulars = regular_players[200:240]
        phase2 = phase2_regulars + cheat_others
        random.shuffle(phase2)
        
        # Phase 3: Picks 250 to 274 -> Next 20 regular players + 5 Cheat Batsmen (Total 25)
        phase3_regulars = regular_players[240:260]
        phase3 = phase3_regulars + cheat_batsmen
        random.shuffle(phase3)
        
        # Phase 4: Picks 275+ -> The rest
        phase4 = regular_players[260:]
        random.shuffle(phase4)
        
        # Combine
        self.cricket_players = phase1 + phase2 + phase3 + phase4"""

replacement = """        cheat_batsmen_names = [
            "Shikhar Dhawan", "David Warner", "Suresh Raina", "Gautam Gambhir", "Shubman Gill"
        ]
        cheat_other_names = [
            "Shane Watson", "Jacques Kallis", "Abhishek Nayar",
            "Dinesh Karthik", "Aditya Tare",
            "Bhuvneshwar Kumar", "Yuzvendra Chahal", "Ravichandran Ashwin", "Amit Mishra", "Sandeep Sharma"
        ]
        backup_cheat_names = [
            "Andre Russell", "Nitish Rana", "Rahul Tripathi", 
            "Kieron Pollard", "Ishan Kishan", "Trent Boult", "Mohammed Shami"
        ]
        
        cheat_batsmen = []
        cheat_others = []
        backup_cheats = []
        regular_players = []
        
        for p in all_cricket_players:
            name = p.get('name')
            if name in cheat_batsmen_names:
                cheat_batsmen.append(p)
            elif name in cheat_other_names:
                cheat_others.append(p)
            elif name in backup_cheat_names:
                backup_cheats.append(p)
            else:
                regular_players.append(p)
                
        # Sort regular players by rating
        regular_players = sorted(regular_players, key=lambda x: x.get('rating', 0), reverse=True)
        
        import random
        
        # Phase 1: Picks 0 to 199 -> Highest rated regular players
        phase1 = regular_players[:200]
        random.shuffle(phase1)
        
        # Phase 2: Picks 200 to 249 -> Next 40 regular players + 10 Cheat Others (Total 50)
        phase2_regulars = regular_players[200:240]
        phase2 = phase2_regulars + cheat_others
        random.shuffle(phase2)
        
        # Phase 3: Picks 250 to 274 -> Next 20 regular players + 5 Cheat Batsmen (Total 25)
        phase3_regulars = regular_players[240:260]
        phase3 = phase3_regulars + cheat_batsmen
        random.shuffle(phase3)
        
        # Phase 4: Picks 275 to 299 -> Next 25 regular players (Total 25)
        phase4 = regular_players[260:285]
        random.shuffle(phase4)

        # Phase 5: Picks 300 to 310 -> Next 4 regular + 7 Backup Cheats (Total 11)
        phase5_regulars = regular_players[285:289]
        phase5 = phase5_regulars + backup_cheats
        random.shuffle(phase5)

        # Phase 6: Picks 311+ -> The rest
        phase6 = regular_players[289:]
        random.shuffle(phase6)
        
        # Combine
        self.cricket_players = phase1 + phase2 + phase3 + phase4 + phase5 + phase6"""

code = code.replace(target, replacement)

with open("game_engine.py", "w") as f:
    f.write(code)

print("Backups rigged.")
