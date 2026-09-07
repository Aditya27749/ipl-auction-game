import re

with open("static/js/app.js", "r") as f:
    js = f.read()

target = """          <div style="display: flex; justify-content: space-between;"><span>1. Structure:</span> <span>${bd.structure.toFixed(1)} / 2.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>2. Overseas Limit:</span> <span>${bd.overseas.toFixed(1)} / 0.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>3. Total Runs:</span> <span>${bd.runs.toFixed(1)} / 3.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>4. Total Wickets:</span> <span>${bd.wickets.toFixed(1)} / 3.5</span></div>
          ${bd.sr_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Strike Rate Penalty:</span> <span>${bd.sr_penalty.toFixed(1)}</span></div>` : ''}
          ${bd.econ_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Economy Penalty:</span> <span>${bd.econ_penalty.toFixed(1)}</span></div>` : ''}"""

replace = """          <div style="display: flex; justify-content: space-between;"><span>1. Structure:</span> <span>${bd.structure.toFixed(1)} / 3.0</span></div>
          <div style="display: flex; justify-content: space-between;"><span>2. Total Runs:</span> <span>${bd.runs.toFixed(1)} / 3.5</span></div>
          <div style="display: flex; justify-content: space-between;"><span>3. Total Wickets:</span> <span>${bd.wickets.toFixed(1)} / 3.5</span></div>
          ${bd.overseas_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Overseas Penalty:</span> <span>${bd.overseas_penalty.toFixed(1)}</span></div>` : ''}
          ${bd.sr_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Strike Rate Penalty:</span> <span>${bd.sr_penalty.toFixed(1)}</span></div>` : ''}
          ${bd.econ_penalty < 0 ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Economy Penalty:</span> <span>${bd.econ_penalty.toFixed(1)}</span></div>` : ''}"""

js = js.replace(target, replace)

with open("static/js/app.js", "w") as f:
    f.write(js)

print("app.js patched")
