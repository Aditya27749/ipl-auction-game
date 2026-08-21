import os
import uuid
import random
import string
import json
import logging
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from models import init_db, create_room, join_room, get_room, get_all_players, update_room_host, remove_player_from_room
from game_engine import AuctionRoom

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database and auto-seed
init_db()

# Auto-seed players if database is empty
from seed_data import seed_players
import subprocess
players = get_all_players()
if not players:
    seed_players()
    logging.info("Database seeded with IPL players from seed_data.py")
    try:
        subprocess.run(["python", "add_100_players.py"], check=True)
        logging.info("Database seeded with 100+ additional players")
    except Exception as e:
        logger.error(f"Failed to add additional 100 players: {e}")

app = FastAPI(title="IPL Auction Arena")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

active_rooms: dict[str, AuctionRoom] = {}

def generate_room_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class CreateRoomReq(BaseModel):
    host_name: str
    max_players: int = 2

class JoinRoomReq(BaseModel):
    player_name: str

@app.post("/api/rooms")
async def api_create_room(req: CreateRoomReq):
    room_code = generate_room_code()
    host_id = str(uuid.uuid4())
    
    create_room(room_code, host_id, req.max_players)
    join_room(room_code, host_id, req.host_name)
    
    # Initialize room engine
    active_rooms[room_code] = AuctionRoom(room_code)
    
    return {"room_code": room_code, "host_id": host_id}

@app.get("/api/rooms/{code}")
async def api_get_room(code: str):
    room = get_room(code)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@app.post("/api/rooms/{code}/join")
async def api_join_room(code: str, req: JoinRoomReq):
    room = get_room(code)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
        
    if room['status'] != 'waiting':
        raise HTTPException(status_code=400, detail="Auction already started")
        
    if len(room['players']) >= room['max_players']:
        raise HTTPException(status_code=400, detail="Room is full")
        
    player_id = str(uuid.uuid4())
    join_room(code, player_id, req.player_name)
    return {"player_id": player_id}

@app.websocket("/ws/{room_code}/{player_id}")
async def websocket_endpoint(websocket: WebSocket, room_code: str, player_id: str):
    await websocket.accept()
    
    room_data = get_room(room_code)
    if not room_data:
        await websocket.send_json({"type": "error", "message": "Room not found"})
        await websocket.close()
        return
        
    # Check if player in room_data
    player_info = next((p for p in room_data['players'] if p['player_id'] == player_id), None)
    if not player_info:
        await websocket.send_json({"type": "error", "message": "Player not found in room"})
        await websocket.close()
        return
        
    if room_code not in active_rooms:
        active_rooms[room_code] = AuctionRoom(room_code)
        
    room = active_rooms[room_code]
    
    room.players[player_id] = {
        "ws": websocket,
        "name": player_info["player_name"],
        "budget": player_info["budget"]
    }
    
    # Broadcast lobby update with normalized player data
    await broadcast_lobby_update(room, room_data['host_id'])
    
    # Sync state if auction is active
    if room.auction_active:
        await room.sync_player_state(player_id)
    
    try:
        while True:
            data = await websocket.receive_text()
            try:
                msg = json.loads(data)
            except json.JSONDecodeError:
                continue
                
            msg_type = msg.get("type")
            
            if msg_type == "start_auction":
                # Verify host
                if room_data['host_id'] == player_id:
                    all_players = get_all_players()
                    if not all_players:
                        await websocket.send_json({"type": "error", "message": "No players in database. Run: python seed_data.py"})
                    else:
                        await room.start_auction(all_players)
                else:
                    await websocket.send_json({"type": "error", "message": "Only host can start auction"})
                    
            elif msg_type == "place_bid":
                amount = float(msg.get("amount", 0))
                success, message = await room.place_bid(player_id, amount)
                if not success:
                    await websocket.send_json({"type": "error", "message": message})
                    
            elif msg_type == "skip_player":
                # Any player can vote to skip, but only process if host
                if room_data['host_id'] == player_id:
                    await room.present_next_player()
                    
            elif msg_type == "sell_player":
                logger.info(f"Received sell_player from {player_id}")
                # Only host can sell
                if room_data['host_id'] == player_id:
                    logger.info("Host authorized, selling player")
                    await room.sell_player()
                else:
                    logger.warning(f"Unauthorized sell attempt from {player_id} (host is {room_data['host_id']})")
                    
            elif msg_type == "kick_player":
                room_data = get_room(room_code)
                if room_data['host_id'] == player_id:
                    target_id = msg.get("target_id")
                    if target_id and target_id in room.players:
                        target_ws = room.players[target_id]["ws"]
                        if target_ws:
                            await target_ws.send_json({"type": "kicked"})
                            await target_ws.close()
                        del room.players[target_id]
                        remove_player_from_room(room_code, target_id)
                        await broadcast_lobby_update(room, room_data['host_id'])
                        
    except WebSocketDisconnect:
        logger.info(f"Client {player_id} disconnected")
        if player_id in room.players:
            room.players[player_id]["ws"] = None
            
        # Host migration if the host disconnects
        room_data = get_room(room_code)
        if room_data and room_data['host_id'] == player_id:
            new_host = None
            for p_id, p_info in room.players.items():
                if p_id != player_id and p_info["ws"] is not None:
                    new_host = p_id
                    break
            if new_host:
                update_room_host(room_code, new_host)
                room_data['host_id'] = new_host
                logger.info(f"Host migrated to {new_host} in room {room_code}")
            
        # Broadcast updated lobby
        if room_data:
            await broadcast_lobby_update(room, room_data['host_id'])
            
        # Clean up if all disconnected and auction is done
        all_disconnected = all(p["ws"] is None for p in room.players.values())
        if all_disconnected:
            if room_code in active_rooms:
                logger.info(f"All players disconnected from room {room_code}, cleaning up")
                del active_rooms[room_code]
    except Exception as e:
        logger.error(f"WebSocket error for {player_id}: {e}")
        if player_id in room.players:
            room.players[player_id]["ws"] = None


async def broadcast_lobby_update(room: AuctionRoom, host_id: str):
    """Send normalized lobby update to all connected players."""
    players_list = []
    for uid, p in room.players.items():
        if p["ws"] is not None:
            players_list.append({
                "name": p["name"],
                "player_id": uid,
                "budget": p["budget"],
                "is_host": uid == host_id
            })
    
    await room.broadcast({
        "type": "lobby_update",
        "players": players_list,
        "host_id": host_id
    })


# Serve static files
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(static_dir, exist_ok=True)

@app.get("/")
async def serve_root():
    return FileResponse(os.path.join(static_dir, "index.html"))

app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"Starting IPL Auction Arena on http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
