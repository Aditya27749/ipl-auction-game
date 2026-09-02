import re

with open("static/js/app.js", "r") as f:
    js = f.read()

new_logic = """function updateAllBudgets(budgets) {
  if (!budgets || !els.auction.allBudgets) return;
  els.auction.allBudgets.innerHTML = '';
  
  for (const [playerId, data] of Object.entries(budgets)) {
    const isMe = playerId === state.playerId;
    const div = document.createElement('div');
    div.className = `budget-pill ${isMe ? 'is-me' : ''}`;
    div.style.flexDirection = 'column';
    div.style.alignItems = 'stretch';
    div.style.borderRadius = '8px';
    div.style.gap = '4px';
    
    const name = typeof data === 'object' ? data.name : 'Player';
    const budget = typeof data === 'object' ? data.budget : data;
    const players = typeof data === 'object' && data.players !== undefined ? data.players : 0;
    const overseas = typeof data === 'object' && data.overseas !== undefined ? data.overseas : 0;
    
    div.innerHTML = `
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <span style="font-weight: bold;">${name} ${isMe ? '(You)' : ''}</span>
        <span style="color: var(--primary-gold); font-weight: bold;">${formatCurrency(budget)}</span>
      </div>
      <div style="display: flex; justify-content: space-between; width: 100%; font-size: 0.75rem; color: var(--text-muted);">
        <span>Players: <span style="color: ${players >= 15 ? 'var(--success-green)' : '#fff'}">${players}/15</span></span>
        <span>Foreign: <span style="color: ${overseas >= 6 ? 'var(--danger-red)' : '#fff'}">${overseas}/6</span></span>
      </div>
    `;
    els.auction.allBudgets.appendChild(div);
  }
}"""

# Use string replace for the whole function
js = re.sub(
    r'function updateAllBudgets\(budgets\) \{[\s\S]*?els\.auction\.allBudgets\.appendChild\(div\);\n  \}\n\}',
    new_logic,
    js
)

with open("static/js/app.js", "w") as f:
    f.write(js)
