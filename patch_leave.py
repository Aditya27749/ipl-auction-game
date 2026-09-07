import re

with open("app.py", "r") as f:
    code = f.read()

target = """            elif msg_type == "kick_player":"""
replace = """            elif msg_type == "leave_room":
                logger.info(f"Player {player_id} intentionally left room {room_code}")
                if player_id in room.players:
                    del room.players[player_id]
                    remove_player_from_room(room_code, player_id)
                room_data = get_room(room_code)
                if room_data:
                    await broadcast_lobby_update(room, room_data['host_id'])
                    
            elif msg_type == "kick_player":"""

code = code.replace(target, replace)

with open("app.py", "w") as f:
    f.write(code)

print("app.py patched")
