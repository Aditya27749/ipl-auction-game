// ================================================
// IPL AUCTION ARENA - Frontend Application
// ================================================

// State management
const state = {
  currentScreen: 'home',
  roomCode: localStorage.getItem('roomCode') || null,
  playerId: localStorage.getItem('playerId') || null,
  playerName: localStorage.getItem('playerName') || null,
  isHost: localStorage.getItem('isHost') === 'true',
  ws: null,
  budget: 120,
  myTeam: [],
  currentAuctionPlayer: null,
  currentBid: 0,
  currentBidder: null,
  currentBidderName: null,
  timerSeconds: 15,
  allBudgets: {},
  auctionIndex: 0,
  totalPlayers: 0,
  hostId: localStorage.getItem('hostId') || null,
  roleColors: {
    'Batsman': '#2196f3',
    'Bowler': '#ef5350',
    'All-Rounder': '#ab47bc',
    'Wicket-Keeper': '#66bb6a'
  }
};

function saveSession() {
  if (state.roomCode) localStorage.setItem('roomCode', state.roomCode);
  if (state.playerId) localStorage.setItem('playerId', state.playerId);
  if (state.playerName) localStorage.setItem('playerName', state.playerName);
  localStorage.setItem('isHost', state.isHost);
  if (state.hostId) localStorage.setItem('hostId', state.hostId);
}

function clearSession() {
  localStorage.clear();
  state.roomCode = null;
  state.playerId = null;
}

// DOM Elements (cached after DOMContentLoaded)
let els = {};

function cacheDOMElements() {
  els = {
    screens: {
      home: document.getElementById('home-screen'),
      lobby: document.getElementById('lobby-screen'),
      auction: document.getElementById('auction-screen'),
      results: document.getElementById('results-screen')
    },
    home: {
      hostName: document.getElementById('host-name'),
      maxPlayers: document.getElementById('max-players'),
      btnCreate: document.getElementById('btn-create-room'),
      joinName: document.getElementById('join-name'),
      roomCode: document.getElementById('room-code'),
      btnJoin: document.getElementById('btn-join-room')
    },
    lobby: {
      displayCode: document.getElementById('display-code'),
      playersList: document.getElementById('lobby-players'),
      btnStart: document.getElementById('btn-start-auction'),
      btnLeave: document.getElementById('btn-leave-room'),
      roomCodeCopy: document.getElementById('lobby-room-code')
    },
    auction: {
      roomCode: document.getElementById('auction-room-code'),
      playerIndex: document.getElementById('player-index'),
      progressFill: document.getElementById('auction-progress'),
      
      // Player Card
      roleBadge: document.getElementById('player-role-badge'),
      natFlag: document.getElementById('player-nat-flag'),
      playerName: document.getElementById('player-name'),
      playerTeam: document.getElementById('player-team'),
      stats: {
        mat: document.getElementById('stat-mat'),
        runs: document.getElementById('stat-runs'),
        wkts: document.getElementById('stat-wkts'),
        sr: document.getElementById('stat-sr'),
        avg: document.getElementById('stat-avg'),
        eco: document.getElementById('stat-eco')
      },
      basePrice: document.getElementById('player-base-price'),
      currBidAmt: document.getElementById('current-bid-amount'),
      currBidder: document.getElementById('current-bidder-name'),
      
      // Timer
      timerText: document.getElementById('timer-seconds'),
      timerRing: document.getElementById('timer-ring'),
      
      // Controls
      btnBid: document.getElementById('btn-place-bid'),
      btnSkip: document.getElementById('btn-skip-bid'),
      btnSell: document.getElementById('btn-sell-player'),
      hostControls: document.getElementById('host-controls'),
      customBid: document.getElementById('custom-bid-input'),
      quickBids: document.querySelectorAll('.btn-quick-bid'),
      
      // Side Panel
      myBudget: document.getElementById('my-budget-amount'),
      slotsFilled: document.getElementById('slots-filled'),
      osFilled: document.getElementById('overseas-filled'),
      myRoster: document.getElementById('my-roster'),
      
      // Bottom Bar
      allBudgets: document.getElementById('all-budgets-list'),
      activityLog: document.getElementById('activity-log'),
      
      // Overlays
      soldOverlay: document.getElementById('sold-overlay'),
      soldTo: document.getElementById('sold-to'),
      soldPrice: document.getElementById('sold-price'),
      unsoldOverlay: document.getElementById('unsold-overlay')
    },
    results: {
      podium: document.getElementById('podium-container'),
      btnPlayAgain: document.getElementById('btn-play-again'),
      btnShare: document.getElementById('btn-share-results')
    },
    toastContainer: document.getElementById('toast-container')
  };
}

// --- API & WebSocket ---
const getApiUrl = () => window.location.origin;
const getWsUrl = () => {
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
  return `${protocol}//${window.location.host}`;
};

// Initialize App
function init() {
  cacheDOMElements();
  bindEvents();
  
  if (state.roomCode && state.playerId) {
    showToast('Reconnecting to room...', 'info');
    connectWebSocket();
  } else {
    showScreen('home');
  }
}

function bindEvents() {
  // Home Screen
  els.home.btnCreate.addEventListener('click', handleCreateRoom);
  els.home.btnJoin.addEventListener('click', handleJoinRoom);
  
  // Enter key on home inputs
  els.home.hostName.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') handleCreateRoom();
  });
  els.home.roomCode.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') handleJoinRoom();
  });
  
  // Lobby
  els.lobby.roomCodeCopy.addEventListener('click', () => copyToClipboard(state.roomCode));
  els.lobby.btnStart.addEventListener('click', handleStartAuction);
  els.lobby.btnLeave.addEventListener('click', disconnectWs);
  
  // Auction - Place Bid button
  els.auction.btnBid.addEventListener('click', () => placeBid(null));
  
  // Skip button sends skip command
  if(els.auction.btnSkip) {
    els.auction.btnSkip.addEventListener('click', () => {
      sendMessage({ type: 'skip_player' });
    });
  }
  
  // Sell button sends sell command
  if(els.auction.btnSell) {
    els.auction.btnSell.addEventListener('click', () => {
      console.log('SELL button clicked! Sending message to server...');
      sendMessage({ type: 'sell_player' });
    });
  }
  
  // Quick bid buttons
  els.auction.quickBids.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const increment = parseFloat(e.target.dataset.amount);
      const baseAmount = state.currentBidder ? state.currentBid : (state.currentAuctionPlayer?.base_price || 0.5);
      placeBid(baseAmount + increment);
    });
  });

  // Keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    if (state.currentScreen !== 'auction') return;
    
    // Don't process if overlay is showing
    const soldHidden = els.auction.soldOverlay.classList.contains('hidden');
    const unsoldHidden = els.auction.unsoldOverlay.classList.contains('hidden');
    if (!soldHidden || !unsoldHidden) return;

    if (e.key === 'Enter') {
      e.preventDefault();
      const customVal = parseFloat(els.auction.customBid.value);
      if (!isNaN(customVal) && customVal > 0) {
        placeBid(customVal);
        els.auction.customBid.value = '';
      } else {
        placeBid(null);
      }
    }
  });
  
  // Results
  els.results.btnPlayAgain.addEventListener('click', () => {
    window.location.reload();
  });
  
  if (els.results.btnShare) {
    els.results.btnShare.addEventListener('click', shareResults);
  }
}

// --- Screen Navigation ---
function showScreen(screenName) {
  Object.values(els.screens).forEach(screen => {
    if (screen) {
      screen.classList.remove('active');
      screen.classList.add('hidden');
    }
  });
  if (els.screens[screenName]) {
    els.screens[screenName].classList.remove('hidden');
    els.screens[screenName].classList.add('active');
  }
  state.currentScreen = screenName;
}

// --- Handlers ---
async function handleCreateRoom() {
  const name = els.home.hostName.value.trim();
  const maxPlayers = parseInt(els.home.maxPlayers.value);
  
  if (!name) return showToast('Please enter your name', 'error');
  if (name.length < 2) return showToast('Name must be at least 2 characters', 'error');
  
  try {
    els.home.btnCreate.disabled = true;
    els.home.btnCreate.innerHTML = '<div class="spinner"></div> Creating...';
    
    const response = await fetch('/api/rooms', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ host_name: name, max_players: maxPlayers })
    });
    
    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.detail || 'Failed to create room');
    }
    
    const data = await response.json();
    state.roomCode = data.room_code;
    state.playerId = data.host_id;
    state.playerName = name;
    state.isHost = true;
    state.hostId = data.host_id;
    saveSession();
    
    connectWebSocket();
  } catch (err) {
    showToast(err.message, 'error');
    els.home.btnCreate.disabled = false;
    els.home.btnCreate.innerHTML = '<span>🚀</span> CREATE ROOM';
  }
}

async function handleJoinRoom() {
  const name = els.home.joinName.value.trim();
  const code = els.home.roomCode.value.trim().toUpperCase();
  
  if (!name) return showToast('Please enter your name', 'error');
  if (!code || code.length < 4) return showToast('Please enter a valid room code', 'error');
  
  try {
    els.home.btnJoin.disabled = true;
    els.home.btnJoin.innerHTML = '<div class="spinner"></div> Joining...';
    
    const response = await fetch(`/api/rooms/${code}/join`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ player_name: name })
    });
    
    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || 'Failed to join room');
    }
    
    const data = await response.json();
    state.roomCode = code;
    state.playerId = data.player_id;
    state.playerName = name;
    state.isHost = false;
    saveSession();
    
    connectWebSocket();
  } catch (err) {
    showToast(err.message, 'error');
    els.home.btnJoin.disabled = false;
    els.home.btnJoin.innerHTML = '<span>🎯</span> JOIN ROOM';
  }
}

// --- WebSocket ---
function connectWebSocket() {
  if (state.ws) {
    state.ws.close();
  }
  
  const wsUrl = `${getWsUrl()}/ws/${state.roomCode}/${state.playerId}`;
  state.ws = new WebSocket(wsUrl);
  
  state.ws.onopen = () => {
    showScreen('lobby');
    els.lobby.displayCode.innerText = state.roomCode;
    if (state.isHost) {
      els.lobby.btnStart.classList.remove('hidden');
    }
    showToast('Connected to room!', 'success');
    if (els.auction.roomCode) {
      els.auction.roomCode.innerText = state.roomCode;
    }
  };
  
  state.ws.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      handleWsMessage(data);
    } catch (e) {
      console.error('Failed to parse WS message:', e);
    }
  };
  
  state.ws.onclose = (event) => {
    if (state.currentScreen !== 'home' && state.currentScreen !== 'results') {
      showToast('Disconnected from server', 'error');
      // Try reconnect after 3 seconds
      setTimeout(() => {
        if (state.currentScreen !== 'home' && state.currentScreen !== 'results') {
          showToast('Attempting to reconnect...', 'info');
          connectWebSocket();
        }
      }, 3000);
    }
  };
  
  state.ws.onerror = (err) => {
    console.error("WS Error:", err);
  };
}

function disconnectWs() {
  clearSession();
  if (state.ws) {
    state.ws.close();
  }
  window.location.reload();
}

function sendMessage(msg) {
  if (state.ws && state.ws.readyState === WebSocket.OPEN) {
    state.ws.send(JSON.stringify(msg));
  } else {
    showToast('Not connected to server', 'error');
  }
}

// --- Message Handlers ---
function handleWsMessage(msg) {
  switch(msg.type) {
    case 'lobby_update':
      if (msg.host_id) state.hostId = msg.host_id;
      updateLobby(msg.players);
      break;
    case 'auction_start':
      showScreen('auction');
      state.totalPlayers = msg.total_players || 0;
      if (msg.budgets) updateAllBudgets(msg.budgets);
      if (state.isHost && els.auction.hostControls) {
          els.auction.hostControls.style.display = 'flex';
      }
      addLogEntry('🏏 Auction started! Let the bidding begin!');
      break;
    case 'new_player':
      renderNewPlayer(msg.player, msg.index, msg.total);
      break;
    case 'timer_update':
      if (document.getElementById('bidding-timer')) {
        document.getElementById('bidding-timer').innerText = msg.seconds;
        if (msg.seconds > 0 && msg.seconds <= 10) playTickSound();

        if (msg.seconds <= 5) {
          document.getElementById('bidding-timer-container').style.color = '#ff4444';
          document.getElementById('bidding-timer-container').style.textShadow = '0 0 10px rgba(255, 68, 68, 0.5)';
        } else {
          document.getElementById('bidding-timer-container').style.color = '#ffeb3b';
          document.getElementById('bidding-timer-container').style.textShadow = '0 0 10px rgba(255, 235, 59, 0.5)';
        }
      }
      break;
    case 'bid_update':
      updateBid(msg.amount, msg.bidder_name, msg.bidder_id);
      break;
    case 'player_sold':
      handlePlayerSold(msg);
      break;
    case 'player_unsold':
      handlePlayerUnsold(msg);
      break;
    case 'budget_update':
      if (msg.budgets) {
        updateAllBudgets(msg.budgets);
        // Update own budget from the budgets dict
        if (msg.budgets[state.playerId]) {
          state.budget = msg.budgets[state.playerId].budget;
          els.auction.myBudget.innerText = formatCurrency(state.budget);
        }
      }
      break;
    case 'kicked':
      clearSession();
      alert('You have been removed from the room by the host.');
      window.location.reload();
      break;
    case 'team_update':
      if (msg.player_id === state.playerId) {
        updateMyTeam(msg.team);
      }
      break;
    case 'auction_end':
      renderResults(msg.results);
      break;
    case 'error':
      showToast(msg.message, 'error');
      break;
    default:
      console.log('Unknown message type:', msg);
  }
}

function confirmKick(targetId, targetName) {
  if (confirm(`Are you sure you want to remove ${targetName} from the room?`)) {
    sendMessage({ type: 'kick_player', target_id: targetId });
  }
}

function updateLobby(players) {
  els.lobby.playersList.innerHTML = '';
  
  if (!players || players.length === 0) {
    els.lobby.playersList.innerHTML = '<div class="empty-roster-msg">No players connected</div>';
    return;
  }
  
  // Check host migration
  const me = players.find(p => p.player_id === state.playerId);
  if (me && me.is_host !== state.isHost) {
    state.isHost = me.is_host;
    saveSession();
    if (state.isHost) {
      showToast('You are now the host!', 'success');
      if (els.auction.hostControls) els.auction.hostControls.style.display = 'flex';
      els.lobby.btnStart.classList.remove('hidden');
    }
  }
  
  players.forEach(p => {
    const isMe = p.player_id === state.playerId;
    const div = document.createElement('div');
    div.className = `player-list-item glass-card ${isMe ? 'is-me' : ''}`;
    
    // Add kick button for host
    const kickHtml = (state.isHost && !isMe) 
      ? `<button class="btn btn-danger" style="padding: 0.2rem 0.5rem; font-size: 0.8rem; margin-left: 10px;" onclick="confirmKick('${p.player_id}', '${p.name || p.player_name || 'Unknown'}')">Kick</button>`
      : '';
      
    div.innerHTML = `
      <span>
        ${p.name || p.player_name || 'Unknown'} 
        ${p.is_host ? '<span class="host-badge">HOST</span>' : ''}
        ${isMe ? '<span style="color:var(--secondary-blue);font-size:0.75rem;"> (You)</span>' : ''}
      </span>
      <div style="display: flex; align-items: center;">
        <span class="budget">₹120 CR</span>
        ${kickHtml}
      </div>
    `;
    els.lobby.playersList.appendChild(div);
  });
  
  // Enable start button for host if 2+ players
  if (state.isHost) {
    els.lobby.btnStart.disabled = players.length < 2;
  } else {
    els.lobby.btnStart.classList.add('hidden');
  }
}

function handleStartAuction() {
  els.lobby.btnStart.disabled = true;
  els.lobby.btnStart.innerHTML = '<div class="spinner"></div> Starting...';
  sendMessage({ type: 'start_auction' });
}

function renderNewPlayer(player, index, total) {
  state.currentAuctionPlayer = player;
  state.currentBid = player.base_price || 0.5;
  state.currentBidder = null;
  state.currentBidderName = null;
  
  // Reset UI
  els.auction.soldOverlay.classList.add('hidden');
  els.auction.unsoldOverlay.classList.add('hidden');
  els.auction.btnBid.disabled = false;
  const quickBtns = document.querySelectorAll('.btn-quick-bid');
  quickBtns.forEach(btn => {
    btn.disabled = false;
    btn.style.opacity = '1';
  });
  
  // Update top bar
  els.auction.playerIndex.innerText = `Player ${index}/${total}`;
  els.auction.progressFill.style.width = `${(index / total) * 100}%`;
  
  // Update Card
  els.auction.playerName.innerText = player.name || 'Unknown';
  els.auction.playerTeam.innerText = player.ipl_team || player.team || '---';
  els.auction.basePrice.innerText = formatCurrency(player.base_price);
  
  // Role badge
  const roleBadge = els.auction.roleBadge;
  const role = player.role || 'Batsman';
  roleBadge.innerText = role;
  roleBadge.style.backgroundColor = state.roleColors[role] || '#2196f3';
  
  // Nationality
  els.auction.natFlag.innerText = player.nationality === 'Indian' ? '🇮🇳' : '🌍';
  
  // Stats
  els.auction.stats.mat.innerText = player.matches ?? '-';
  els.auction.stats.runs.innerText = player.runs ?? '-';
  els.auction.stats.wkts.innerText = player.wickets ?? '-';
  els.auction.stats.sr.innerText = player.strike_rate ? player.strike_rate.toFixed(1) : '-';
  els.auction.stats.avg.innerText = player.batting_avg ? player.batting_avg.toFixed(1) : '-';
  els.auction.stats.eco.innerText = player.economy ? player.economy.toFixed(1) : '-';
  
  // Reset Bids
  els.auction.currBidAmt.innerText = formatCurrency(player.base_price);
  els.auction.currBidder.innerText = 'Waiting for bids...';
  els.auction.currBidder.style.color = 'var(--text-secondary)';
  
  addLogEntry(`🏏 Up for auction: <strong>${player.name}</strong> (Base: ${formatCurrency(player.base_price)})`);
}

function updateBid(amount, bidderName, bidderId) {
  playBidSound();

  state.currentBid = amount;
  state.currentBidder = bidderId;
  state.currentBidderName = bidderName;
  
  // Animate the bid amount
  els.auction.currBidAmt.innerText = formatCurrency(amount);
  els.auction.currBidAmt.style.animation = 'none';
  els.auction.currBidAmt.offsetHeight; // trigger reflow
  els.auction.currBidAmt.style.animation = 'pulse 0.3s ease';
  // Update quick bid buttons based on current bid
  const quickBtns = document.querySelectorAll('.btn-quick-bid');
  quickBtns.forEach(btn => {
    const amt = parseFloat(btn.getAttribute('data-amount'));
    if ((amount >= 3.0 && amt === 0.25) || (amount >= 6.0 && amt === 0.5)) {
      btn.disabled = true;
      btn.style.opacity = '0.3';
    } else {
      btn.disabled = false;
      btn.style.opacity = '1';
    }
  });
  
  // Show who holds the bid
  if (bidderId === state.playerId) {
    els.auction.currBidder.innerText = '✅ You are the highest bidder!';
    els.auction.currBidder.style.color = 'var(--success-green)';
  } else {
    els.auction.currBidder.innerText = `${bidderName} holds the bid`;
    els.auction.currBidder.style.color = 'var(--secondary-blue)';
  }
  
  addLogEntry(`💰 ${bidderName} bid ${formatCurrency(amount)}`);
}



function placeBid(amount) {
  if (!state.currentAuctionPlayer) return;
  
  // If no amount passed, calculate default increment
  if (amount === null || amount === undefined) {
    if (!state.currentBidder) {
      // First bid = base price
      amount = state.currentAuctionPlayer.base_price;
    } else {
      // Auto-increment based on current bid
      let increment = 0.25;
      if (state.currentBid >= 10) increment = 0.5;
      if (state.currentBid >= 20) increment = 1.0;
      if (state.currentBid >= 50) increment = 2.0;
      amount = state.currentBid + increment;
    }
  }
  
  // Round to 2 decimal places
  amount = Math.round(amount * 100) / 100;
  
  // Client-side validation
  if (amount > state.budget) {
    return showToast('Insufficient budget!', 'error');
  }
  
  if (state.myTeam.length >= 15) {
    return showToast('Team roster is full (15/15)!', 'error');
  }
  
  if (state.currentBidder === state.playerId && amount <= state.currentBid) {
    return showToast('You are already the highest bidder!', 'info');
  }
  
  sendMessage({ type: 'place_bid', amount: amount });
}

function handlePlayerSold(msg) {
  playSoldSound();

  els.auction.btnBid.disabled = true;
  
  const isBuyer = msg.buyer_id === state.playerId;
  els.auction.soldTo.innerText = isBuyer ? 'YOU! 🎉' : (msg.buyer_name || 'Unknown');
  els.auction.soldPrice.innerText = formatCurrency(msg.amount || msg.price);
  
  els.auction.soldOverlay.classList.remove('hidden');
  
  const playerName = msg.player?.name || 'Unknown';
  const buyerName = isBuyer ? 'YOU' : (msg.buyer_name || 'Unknown');
  addLogEntry(`🔨 <strong>SOLD!</strong> ${playerName} to ${buyerName} for ${formatCurrency(msg.amount || msg.price)}`);
}

function handlePlayerUnsold(msg) {
  playUnsoldSound();

  els.auction.btnBid.disabled = true;
  els.auction.unsoldOverlay.classList.remove('hidden');
  addLogEntry(`❌ ${msg.player?.name || 'Player'} went UNSOLD`);
}

function updateMyTeam(team) {
  state.myTeam = team || [];
  els.auction.myRoster.innerHTML = '';
  
  if (state.myTeam.length === 0) {
    els.auction.myRoster.innerHTML = '<div class="empty-roster-msg">No players bought yet.</div>';
    return;
  }
  
  let osCount = 0;
  state.myTeam.forEach((p, index) => {
    if (p.nationality && p.nationality !== 'Indian') osCount++;
    
    const div = document.createElement('div');
    div.className = 'roster-item';
    const roleColor = state.roleColors[p.role] || '#2196f3';
    const isImpact = index === 14;
    div.innerHTML = `
      <div class="name">
        <span style="color: ${roleColor}">●</span> 
        ${p.name} ${p.nationality !== 'Indian' ? '✈️' : ''}
        ${isImpact ? '<span style="color:var(--warning-yellow);font-size:0.7rem;"> IMPACT</span>' : ''}
      </div>
      <div class="price">${formatCurrency(p.bought_price || p.price_paid || 0)}</div>
    `;
    els.auction.myRoster.appendChild(div);
  });
  
  els.auction.slotsFilled.innerText = state.myTeam.length;
  els.auction.osFilled.innerText = osCount;
}

function updateAllBudgets(budgets) {
  if (!budgets || !els.auction.allBudgets) return;
  els.auction.allBudgets.innerHTML = '';
  
  for (const [playerId, data] of Object.entries(budgets)) {
    const isMe = playerId === state.playerId;
    const div = document.createElement('div');
    div.className = `budget-pill ${isMe ? 'is-me' : ''}`;
    const name = typeof data === 'object' ? data.name : 'Player';
    const budget = typeof data === 'object' ? data.budget : data;
    div.innerHTML = `
      ${name} ${isMe ? '(You)' : ''}
      <span>${formatCurrency(budget)}</span>
    `;
    els.auction.allBudgets.appendChild(div);
  }
}

function addLogEntry(text) {
  if (!els.auction.activityLog) return;
  const div = document.createElement('div');
  div.className = 'log-entry';
  div.innerHTML = text;
  els.auction.activityLog.appendChild(div);
  els.auction.activityLog.scrollTop = els.auction.activityLog.scrollHeight;
  
  // Keep only last 15 entries
  while (els.auction.activityLog.children.length > 15) {
    els.auction.activityLog.removeChild(els.auction.activityLog.firstChild);
  }
}

function renderResults(results) {
  showScreen('results');
  triggerConfetti();
  
  if (!els.results.podium) return;
  els.results.podium.innerHTML = '';
  
  results.forEach((res, index) => {
    const rank = index + 1;
    let badge = `#${rank}`;
    if (rank === 1) badge = '🥇';
    if (rank === 2) badge = '🥈';
    if (rank === 3) badge = '🥉';
    
    const isMe = res.user_id === state.playerId;
    const score = res.score || 0;
    
    // Build team roster HTML
    let teamHTML = '';
    if (res.team && res.team.length > 0) {
      teamHTML = '<div class="result-team-roster">';
      res.team.forEach((p, i) => {
        const roleColor = state.roleColors[p.role] || '#2196f3';
        const isImpact = i === 14;
        teamHTML += `
          <div class="result-team-player">
            <span style="color:${roleColor}">●</span>
            ${p.name} ${p.nationality !== 'Indian' ? '✈️' : ''}
            ${isImpact ? '<span style="color:var(--warning-yellow);font-size:0.7rem;">IMPACT</span>' : ''}
            <span style="color:var(--primary-gold);margin-left:auto;">${formatCurrency(p.bought_price || 0)}</span>
          </div>
        `;
      });
      teamHTML += '</div>';
    }
    
    const card = document.createElement('div');
    card.className = `rank-card ${rank === 1 ? 'rank-1' : ''} ${isMe ? 'is-me' : ''}`;
    
    card.innerHTML = `
      <div class="rank-badge">${badge}</div>
      <h3>${res.player_name || 'Player'} ${isMe ? '(You)' : ''}</h3>
      <p>Budget remaining: ${formatCurrency(res.budget_remaining || 0)}</p>
      <p>Players drafted: ${res.team_size || (res.team ? res.team.length : 0)}/12</p>
      <div class="score-circle">${score.toFixed(1)}</div>
      <p style="margin-top:8px;font-size:0.8rem;color:var(--text-muted);">out of 10</p>
      ${teamHTML}
    `;
    
    els.results.podium.appendChild(card);
  });
}

// --- Utilities ---
function formatCurrency(amount) {
  const num = parseFloat(amount);
  if (isNaN(num)) return '₹0.00 CR';
  return `₹${num.toFixed(2)} CR`;
}

function copyToClipboard(text) {
  if (!text) return;
  navigator.clipboard.writeText(text).then(() => {
    showToast('Room code copied to clipboard!', 'success');
  }).catch(err => {
    // Fallback for older browsers
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    showToast('Room code copied!', 'success');
  });
}

function showToast(message, type = 'info') {
  if (!els.toastContainer) return;
  
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerText = message;
  
  els.toastContainer.appendChild(toast);
  
  setTimeout(() => {
    if (toast.parentElement) {
      toast.style.animation = 'fadeIn 0.3s ease reverse';
      setTimeout(() => toast.remove(), 300);
    }
  }, 3000);
}

function triggerConfetti() {
  const container = document.getElementById('confetti-container');
  if (!container) return;
  container.innerHTML = '';
  
  const colors = ['#f5a623', '#00d4ff', '#00e676', '#ff5252', '#ab47bc', '#ffab40', '#ffffff'];
  
  for (let i = 0; i < 60; i++) {
    const piece = document.createElement('div');
    piece.className = 'confetti-piece';
    piece.style.left = `${Math.random() * 100}%`;
    piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    piece.style.animationDuration = `${2 + Math.random() * 3}s`;
    piece.style.animationDelay = `${Math.random() * 2}s`;
    piece.style.width = `${6 + Math.random() * 8}px`;
    piece.style.height = `${6 + Math.random() * 8}px`;
    piece.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    piece.style.transform = `rotate(${Math.random() * 360}deg)`;
    container.appendChild(piece);
  }
}

function shareResults() {
  const text = `🏏 IPL Auction Arena Results!\nRoom: ${state.roomCode}\nCheck it out at ${window.location.origin}`;
  
  if (navigator.share) {
    navigator.share({ title: 'IPL Auction Arena Results', text: text });
  } else {
    copyToClipboard(text);
    showToast('Results copied to clipboard!', 'success');
  }
}

// Init
document.addEventListener('DOMContentLoaded', init);



// --- Advanced Audio System (Improved IPL Tune) ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
const GLOBAL_VOLUME = 0.15; // Slightly bumped up but still soft

function playHornTone(freq, duration, delay) {
    if(audioCtx.state === 'suspended') return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    
    // Trumpet-like settings
    osc.type = 'sawtooth';
    filter.type = 'lowpass';
    
    // Brass filter envelope
    filter.frequency.setValueAtTime(500, audioCtx.currentTime + delay);
    filter.frequency.linearRampToValueAtTime(3000, audioCtx.currentTime + delay + 0.05);
    filter.frequency.linearRampToValueAtTime(1000, audioCtx.currentTime + delay + duration);
    
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime + delay);
    
    // Volume envelope (ADSR)
    gain.gain.setValueAtTime(0, audioCtx.currentTime + delay);
    gain.gain.linearRampToValueAtTime(1.0 * GLOBAL_VOLUME, audioCtx.currentTime + delay + 0.03); // Attack
    gain.gain.linearRampToValueAtTime(0.8 * GLOBAL_VOLUME, audioCtx.currentTime + delay + 0.1);  // Decay
    gain.gain.setValueAtTime(0.8 * GLOBAL_VOLUME, audioCtx.currentTime + delay + duration - 0.05); // Sustain
    gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + delay + duration); // Release
    
    osc.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start(audioCtx.currentTime + delay);
    osc.stop(audioCtx.currentTime + delay + duration);
}

const iplHornAudio = new Audio("/static/ipl_horn.webm");
iplHornAudio.volume = 0.15;

function playSoldSound() {
    if(audioCtx.state === "suspended") audioCtx.resume();
    iplHornAudio.currentTime = 0;
    iplHornAudio.play().catch(e => console.log("Audio play failed:", e));
    setTimeout(() => {
        iplHornAudio.pause();
        iplHornAudio.currentTime = 0;
    }, 4000);
    const thud = audioCtx.createOscillator();
    const gainThud = audioCtx.createGain();
    thud.type = "sine";
    thud.frequency.setValueAtTime(150, audioCtx.currentTime);
    thud.frequency.exponentialRampToValueAtTime(10, audioCtx.currentTime + 0.15);
    gainThud.gain.setValueAtTime(1.5 * GLOBAL_VOLUME, audioCtx.currentTime);
    gainThud.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
    thud.connect(gainThud);
    gainThud.connect(audioCtx.destination);
    thud.start();
    thud.stop(audioCtx.currentTime + 0.15);
}

    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    // Clean, crisp digital bell
    osc.type = 'sine';
    osc.frequency.setValueAtTime(1800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(600, audioCtx.currentTime + 0.15);
    
    gain.gain.setValueAtTime(0.6 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.15);
}

function playUnsoldSound() {
    if(audioCtx.state === 'suspended') audioCtx.resume();
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(150, audioCtx.currentTime);
    osc.frequency.linearRampToValueAtTime(80, audioCtx.currentTime + 0.6);
    
    gain.gain.setValueAtTime(0.4 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 0.6);
    
    // Add a lowpass filter to make it sound muffled/sad
    const filter = audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(800, audioCtx.currentTime);
    filter.frequency.linearRampToValueAtTime(200, audioCtx.currentTime + 0.6);
    
    osc.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.6);
}

function playTickSound() {
    if(audioCtx.state === 'suspended') return;
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    // Wooden clock tick
    osc.type = 'square';
    osc.frequency.setValueAtTime(800, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.05);
    
    gain.gain.setValueAtTime(0.3 * GLOBAL_VOLUME, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
    
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc.start();
    osc.stop(audioCtx.currentTime + 0.05);
}
