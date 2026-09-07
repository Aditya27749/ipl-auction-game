import re

with open("static/js/app.js", "r") as f:
    js = f.read()

target = """          ${bd.mission_status === 'Success' ? `<div style="display: flex; justify-content: space-between; color: var(--success-green);"><span>Mission Success (${bd.secret_captain}):</span> <span>+0.5</span></div>` : ''}"""
replace = """          ${bd.mission_status === 'Success' ? `<div style="display: flex; justify-content: space-between; color: var(--success-green);"><span>Mission Success (${bd.secret_captain}):</span> <span>+0.0 (No Penalty)</span></div>` : ''}"""

js = js.replace(target, replace)

with open("static/js/app.js", "w") as f:
    f.write(js)

print("JS patched.")
