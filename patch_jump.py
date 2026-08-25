with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
for line in lines:
    if "async def present_next_player(self):" in line:
        new_method = """    async def jump_to_player(self, search_name: str) -> tuple[bool, str]:
        \"\"\"Find a player by name and move them to be the very next player auctioned.\"\"\"
        if not self.auction_active:
            return False, "Auction not active"
            
        search_lower = search_name.lower().strip()
        found_index = -1
        
        # Search forward from the NEXT player to the end of the deck
        start_search = self.current_player_index + 1
        for i in range(start_search, len(self.cricket_players)):
            if search_lower in self.cricket_players[i]['name'].lower():
                found_index = i
                break
                
        if found_index != -1:
            # Pop the player from their current position and insert at next position
            player = self.cricket_players.pop(found_index)
            self.cricket_players.insert(self.current_player_index + 1, player)
            return True, f"Success! {player['name']} will be auctioned next."
        else:
            return False, f"Could not find any unsold player matching '{search_name}'"

"""
        out.append(new_method)
    out.append(line)

with open("game_engine.py", "w") as f:
    f.writelines(out)
