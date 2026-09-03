import re

with open("static/js/app.js", "r") as f:
    js = f.read()

new_logic = """    const overseas = typeof data === 'object' && data.overseas !== undefined ? data.overseas : 0;
    const teamName = typeof data === 'object' && data.ipl_team ? data.ipl_team : '';
    
    div.innerHTML = `
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <span style="font-weight: bold;">${name} <span style="font-size:0.7rem; color:#00d4ff;">${teamName ? '[' + teamName.split(' ').map(w=>w[0]).join('') + ']' : ''}</span> ${isMe ? '(You)' : ''}</span>
        <span style="color: var(--primary-gold); font-weight: bold;">${formatCurrency(budget)}</span>
      </div>
      <div style="display: flex; justify-content: space-between; width: 100%; font-size: 0.75rem; color: var(--text-muted);">
        <span>Players: <span style="color: ${players >= 15 ? 'var(--success-green)' : '#fff'}">${players}/15</span></span>
        <span>Foreign: <span style="color: ${overseas >= 6 ? 'var(--danger-red)' : '#fff'}">${overseas}/6</span></span>
      </div>
    `;"""

js = js.replace("""    const overseas = typeof data === 'object' && data.overseas !== undefined ? data.overseas : 0;
    
    div.innerHTML = `
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <span style="font-weight: bold;">${name} ${isMe ? '(You)' : ''}</span>
        <span style="color: var(--primary-gold); font-weight: bold;">${formatCurrency(budget)}</span>
      </div>
      <div style="display: flex; justify-content: space-between; width: 100%; font-size: 0.75rem; color: var(--text-muted);">
        <span>Players: <span style="color: ${players >= 15 ? 'var(--success-green)' : '#fff'}">${players}/15</span></span>
        <span>Foreign: <span style="color: ${overseas >= 6 ? 'var(--danger-red)' : '#fff'}">${overseas}/6</span></span>
      </div>
    `;""", new_logic)

with open("static/js/app.js", "w") as f:
    f.write(js)
