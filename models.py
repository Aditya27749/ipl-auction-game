import sqlite3
import os

DB_PATH = "ipl_auction.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL UNIQUE,
      nationality TEXT NOT NULL,
      role TEXT NOT NULL,
      bowling_style TEXT,
      ipl_team TEXT,
      matches INTEGER DEFAULT 0,
      runs INTEGER DEFAULT 0,
      wickets INTEGER DEFAULT 0,
      batting_avg REAL DEFAULT 0,
      bowling_avg REAL DEFAULT 0,
      strike_rate REAL DEFAULT 0,
      economy REAL DEFAULT 0,
      base_price REAL DEFAULT 0.5,
      rating REAL DEFAULT 5.0,
      image_url TEXT DEFAULT ''
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
      id TEXT PRIMARY KEY,
      host_id TEXT NOT NULL,
      max_players INTEGER DEFAULT 2,
      status TEXT DEFAULT 'waiting',
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS room_players (
      room_id TEXT NOT NULL,
      player_id TEXT NOT NULL,
      player_name TEXT NOT NULL,
      budget REAL DEFAULT 120.0,
      team_score REAL DEFAULT 0,
      PRIMARY KEY (room_id, player_id),
      FOREIGN KEY (room_id) REFERENCES rooms(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS drafted_players (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      room_id TEXT NOT NULL,
      user_id TEXT NOT NULL,
      cricket_player_id INTEGER NOT NULL,
      price_paid REAL NOT NULL,
      pick_order INTEGER NOT NULL,
      is_impact_player BOOLEAN DEFAULT 0,
      FOREIGN KEY (room_id) REFERENCES rooms(id),
      FOREIGN KEY (cricket_player_id) REFERENCES players(id)
    )
    ''')

    conn.commit()
    conn.close()

def get_all_players():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    players = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return players

def create_room(room_id, host_id, max_players):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO rooms (id, host_id, max_players) VALUES (?, ?, ?)",
        (room_id, host_id, max_players)
    )
    conn.commit()
    conn.close()

def join_room(room_id, player_id, player_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO room_players (room_id, player_id, player_name) VALUES (?, ?, ?)",
        (room_id, player_id, player_name)
    )
    conn.commit()
    conn.close()

def get_room(room_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM rooms WHERE id = ?", (room_id,))
    room_row = cursor.fetchone()
    
    if not room_row:
        conn.close()
        return None
        
    room = dict(room_row)
    
    cursor.execute("SELECT * FROM room_players WHERE room_id = ?", (room_id,))
    players = [dict(row) for row in cursor.fetchall()]
    room['players'] = players
    
    conn.close()
    return room

def update_room_status(room_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET status = ? WHERE id = ?", (status, room_id))
    conn.commit()
    conn.close()

def update_room_host(room_id, new_host_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET host_id = ? WHERE id = ?", (new_host_id, room_id))
    conn.commit()
    conn.close()

def remove_player_from_room(room_id, player_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM room_players WHERE room_id = ? AND player_id = ?", (room_id, player_id))
    conn.commit()
    conn.close()

def update_player_budget(room_id, player_id, new_budget):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE room_players SET budget = ? WHERE room_id = ? AND player_id = ?",
        (new_budget, room_id, player_id)
    )
    conn.commit()
    conn.close()

def update_team_score(room_id, player_id, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE room_players SET team_score = ? WHERE room_id = ? AND player_id = ?",
        (score, room_id, player_id)
    )
    conn.commit()
    conn.close()

def draft_player(room_id, user_id, cricket_player_id, price, pick_order, is_impact):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO drafted_players 
           (room_id, user_id, cricket_player_id, price_paid, pick_order, is_impact_player) 
           VALUES (?, ?, ?, ?, ?, ?)""",
        (room_id, user_id, cricket_player_id, price, pick_order, is_impact)
    )
    conn.commit()
    conn.close()

def get_drafted_players(room_id, user_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """SELECT d.*, p.* 
           FROM drafted_players d 
           JOIN players p ON d.cricket_player_id = p.id 
           WHERE d.room_id = ? AND d.user_id = ?
           ORDER BY d.pick_order ASC""",
        (room_id, user_id)
    )
    players = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return players

def get_all_drafted(room_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """SELECT d.*, p.* 
           FROM drafted_players d 
           JOIN players p ON d.cricket_player_id = p.id 
           WHERE d.room_id = ?
           ORDER BY d.pick_order ASC""",
        (room_id,)
    )
    players = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return players
