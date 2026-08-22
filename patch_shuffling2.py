with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if "# Divide into 3 perfectly balanced tiers" in line:
        skip = True
        
    if skip and "self.current_player_index = -1" in line:
        skip = False
        new_logic = """        # Sort all players by rating (highest first)
        sorted_players = sorted(all_cricket_players, key=lambda x: x.get('rating', 0), reverse=True)
        
        # Take the top 120 players (All Legends and Main Stars)
        main_players = sorted_players[:120]
        
        # Take the remaining players (Uncapped / Base Price)
        remaining_players = sorted_players[120:]
        
        import random
        random.shuffle(main_players)
        random.shuffle(remaining_players)
        
        # Combine them so ALL main players appear in the first 120 slots!
        self.cricket_players = main_players + remaining_players
        
"""
        out.append(new_logic)
        
    if not skip:
        out.append(line)

with open("game_engine.py", "w") as f:
    f.writelines(out)
