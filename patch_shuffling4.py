with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if "cheat_names = [" in line:
        skip = True
        new_logic = """        cheat_names = [
            "Shikhar Dhawan", "David Warner", "Suresh Raina", "Gautam Gambhir", "Shubman Gill",
            "Shane Watson", "Jacques Kallis", "Abhishek Nayar",
            "Dinesh Karthik", "Aditya Tare",
            "Bhuvneshwar Kumar", "Yuzvendra Chahal", "Ravichandran Ashwin", "Amit Mishra", "Sandeep Sharma"
        ]
        
        cheat_players = []
        regular_players = []
        
        for p in all_cricket_players:
            if p.get('name') in cheat_names:
                cheat_players.append(p)
            else:
                regular_players.append(p)
                
        # Sort regular players by rating
        regular_players = sorted(regular_players, key=lambda x: x.get('rating', 0), reverse=True)
        
        import random
        
        # Phase 1: First 200 players (0 to 199) -> Highest rated regular players
        phase1 = regular_players[:200]
        random.shuffle(phase1)
        
        # Phase 2: Picks 200 to 250 -> Next 35 regular players + 15 Cheat Players (Total 50)
        phase2_regulars = regular_players[200:235]
        phase2 = phase2_regulars + cheat_players
        random.shuffle(phase2)
        
        # Phase 3: Picks 250+ -> The rest
        phase3 = regular_players[235:]
        random.shuffle(phase3)
        
        # Combine
        self.cricket_players = phase1 + phase2 + phase3
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
