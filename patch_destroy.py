with open("app.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if 'elif msg_type == "place_bid":' in line:
        # Insert destroy_room logic right before place_bid
        new_logic = """            elif msg_type == "destroy_room":
                if room_data['host_id'] == player_id:
                    logger.info(f"Host {player_id} destroyed room {room_code}")
                    await room.broadcast({"type": "room_destroyed", "message": "The host has destroyed the room."})
                    
                    # Give clients a brief moment to receive the message before closing
                    await asyncio.sleep(0.5)
                    
                    for p_info in room.players.values():
                        if p_info["ws"]:
                            try:
                                await p_info["ws"].close()
                            except:
                                pass
                                
                    if room_code in active_rooms:
                        del active_rooms[room_code]
                        
                    from models import get_connection
                    conn = get_connection()
                    conn.execute("DELETE FROM rooms WHERE id = ?", (room_code,))
                    conn.execute("DELETE FROM drafted_players WHERE room_id = ?", (room_code,))
                    conn.commit()
                    conn.close()
                else:
                    await websocket.send_json({"type": "error", "message": "Only the host can destroy the room."})
                    
"""
        out.append(new_logic)
        
    out.append(line)

with open("app.py", "w") as f:
    f.writelines(out)
