with open("app.py", "r") as f:
    lines = f.readlines()

out = []
for line in lines:
    if 'elif msg_type == "sell_player":' in line:
        new_logic = """            elif msg_type == "jump_player":
                if room_data['host_id'] == player_id:
                    search_name = msg.get("name", "")
                    success, message = await room.jump_to_player(search_name)
                    if success:
                        await websocket.send_json({"type": "success", "message": message})
                        # If auction is waiting or current player is empty, maybe present them immediately?
                        # But standard is they just click SKIP to go to next.
                    else:
                        await websocket.send_json({"type": "error", "message": message})
                else:
                    await websocket.send_json({"type": "error", "message": "Only host can jump players"})
                    
"""
        out.append(new_logic)
    out.append(line)

with open("app.py", "w") as f:
    f.writelines(out)
