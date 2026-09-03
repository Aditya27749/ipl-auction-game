with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if "cheat_names = [" in line:
        skip = True
        new_logic = """        cheat_batsmen_names = [
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
        self.cricket_players = phase1 + phase2 + phase3 + phase4
"""
        out.append(new_logic)
        continue
        
    if skip and "self.current_player_index = 0" in line:
        skip = False
        out.append("        self.current_player_index = 0\n")
        continue
        
    if not skip:
        out.append(line)

with open("game_engine.py", "w") as f:
    f.writelines(out)
