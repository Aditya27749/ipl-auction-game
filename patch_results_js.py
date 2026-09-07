import re

with open("static/js/app.js", "r") as f:
    js = f.read()

target = """    // Build team roster HTML
    let teamHTML = '';
    if (res.team && res.team.length > 0) {"""

replace = """    // Build score breakdown HTML
    let breakdownHTML = '';
    if (res.score_breakdown) {
      const bd = res.score_breakdown;
      breakdownHTML = `
        <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; margin: 15px 0; font-size: 0.85rem; font-family: monospace;">
          <div style="color: var(--primary-gold); margin-bottom: 5px; font-weight: bold; text-align: center;">AI PREDICTOR BREAKDOWN</div>
          <div style="display: flex; justify-content: space-between;"><span>1. Structure:</span> <span>${bd.structure.toFixed(1)} / 2.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>2. Overseas Limit:</span> <span>${bd.overseas.toFixed(1)} / 0.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>3. Total Runs:</span> <span>${bd.runs.toFixed(1)} / 3.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>4. Total Wickets:</span> <span>${bd.wickets.toFixed(1)} / 3.5</span></div>
          ${bd.sr_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Strike Rate Penalty:</span> <span>${bd.sr_penalty.toFixed(1)}</span></div>` : ''}
          ${bd.econ_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Economy Penalty:</span> <span>${bd.econ_penalty.toFixed(1)}</span></div>` : ''}
          ${bd.bonus > 0 ? `<div style="display: flex; justify-content: space-between; color: var(--success-green);"><span>Secret Mission Bonus:</span> <span>+${bd.bonus.toFixed(1)}</span></div>` : ''}
        </div>
      `;
    }

    // Build team roster HTML
    let teamHTML = '';
    if (res.team && res.team.length > 0) {"""

js = js.replace(target, replace)

target2 = """      teamHTML += '</div>';
    }
    
    const div = document.createElement('div');
    div.className = `result-card ${isMe ? 'is-me' : ''}`;
    div.innerHTML = `
      <div class="result-header">
        <div class="result-rank">${badge}</div>
        <div class="result-name">${res.player_name} ${isMe ? '(You)' : ''}</div>
        <div class="result-score">${score.toFixed(1)} <span style="font-size: 0.8rem; opacity: 0.7;">/ 10.0</span></div>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 10px;">
        <span>Players: ${res.team_size}/15</span>
        <span>Budget Left: ${formatCurrency(res.budget_remaining || 0)}</span>
      </div>
      ${teamHTML}
    `;"""

replace2 = """      teamHTML += '</div>';
    }
    
    const div = document.createElement('div');
    div.className = `result-card ${isMe ? 'is-me' : ''}`;
    div.innerHTML = `
      <div class="result-header">
        <div class="result-rank">${badge}</div>
        <div class="result-name">${res.player_name} ${isMe ? '(You)' : ''}</div>
        <div class="result-score">${score.toFixed(1)} <span style="font-size: 0.8rem; opacity: 0.7;">/ 10.0</span></div>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 10px;">
        <span>Players: ${res.team_size}/15</span>
        <span>Budget Left: ${formatCurrency(res.budget_remaining || 0)}</span>
      </div>
      ${breakdownHTML}
      ${teamHTML}
    `;"""

js = js.replace(target2, replace2)

with open("static/js/app.js", "w") as f:
    f.write(js)

print("JS patched.")
