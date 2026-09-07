import re

with open("static/js/app.js", "r") as f:
    js = f.read()

target = """          ${bd.bonus > 0 ? `<div style="display: flex; justify-content: space-between; color: var(--success-green);"><span>Secret Mission Bonus:</span> <span>+${bd.bonus.toFixed(1)}</span></div>` : ''}"""

replace = """          ${bd.mission_status === 'Success' ? `<div style="display: flex; justify-content: space-between; color: var(--success-green);"><span>Mission Success (${bd.secret_captain}):</span> <span>+0.5</span></div>` : ''}
          ${bd.mission_status === 'Failed' ? `<div style="display: flex; justify-content: space-between; color: var(--danger-red);"><span>Mission Failed (${bd.secret_captain}):</span> <span>-0.5</span></div>` : ''}"""

js = js.replace(target, replace)

with open("static/js/app.js", "w") as f:
    f.write(js)

print("app.js mission patched")
