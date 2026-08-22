with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if "# Separate legends" in line:
        skip = True
        
    if skip and "self.current_player_index = -1" in line:
        skip = False
        # Insert new shuffling logic here
        new_logic = """        # Divide into 3 perfectly balanced tiers
        legends = [p for p in all_cricket_players if p.get('rating', 0) >= 9.0]
        stars = [p for p in all_cricket_players if 8.0 <= p.get('rating', 0) < 9.0]
        uncapped = [p for p in all_cricket_players if p.get('rating', 0) < 8.0]
        
        import random
        random.shuffle(legends)
        random.shuffle(stars)
        random.shuffle(uncapped)
        
        self.cricket_players = []
        
        # Build perfectly balanced "sets" of 10 players
        # 1 Legend, 4 Stars, 5 Uncapped
        while legends or stars or uncapped:
            set_players = []
            if legends:
                set_players.append(legends.pop(0))
            elif stars:
                set_players.append(stars.pop(0))
                
            for _ in range(4):
                if stars:
                    set_players.append(stars.pop(0))
                elif uncapped:
                    set_players.append(uncapped.pop(0))
                    
            for _ in range(5):
                if uncapped:
                    set_players.append(uncapped.pop(0))
                elif stars:
                    set_players.append(stars.pop(0))
                    
            # Shuffle the mini-set so the legend isn't ALWAYS the first player
            random.shuffle(set_players)
            self.cricket_players.extend(set_players)
            
"""
        out.append(new_logic)
        
    if not skip:
        out.append(line)

with open("game_engine.py", "w") as f:
    f.writelines(out)
