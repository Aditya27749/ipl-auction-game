import re

with open("static/js/app.js", "r") as f:
    js = f.read()

target = """        <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; margin: 15px 0; font-size: 0.85rem; font-family: monospace;">
          <div style="color: var(--primary-gold); margin-bottom: 5px; font-weight: bold; text-align: center;">AI PREDICTOR BREAKDOWN</div>"""

replace = """        <div style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; margin: 15px 0; font-size: 0.85rem; font-family: monospace;">
          <div style="color: #64ffda; margin-bottom: 5px; font-weight: bold; text-align: center;">RAW SQUAD STATS</div>
          <div style="display: flex; justify-content: space-between;"><span>Total Runs:</span> <span>${bd.raw_runs}</span></div>
          <div style="display: flex; justify-content: space-between;"><span>Total Wickets:</span> <span>${bd.raw_wickets}</span></div>
          <div style="display: flex; justify-content: space-between;"><span>Avg Strike Rate:</span> <span style="color: ${bd.raw_sr >= 133.0 ? 'var(--success-green)' : 'var(--danger-red)'}">${bd.raw_sr}</span></div>
          <div style="display: flex; justify-content: space-between;"><span>Avg Economy:</span> <span style="color: ${bd.raw_econ <= 8.00 ? 'var(--success-green)' : 'var(--danger-red)'}">${bd.raw_econ}</span></div>
          
          <hr style="border-color: rgba(255,255,255,0.1); margin: 8px 0;">
          
          <div style="color: var(--primary-gold); margin-bottom: 5px; font-weight: bold; text-align: center;">AI PREDICTOR BREAKDOWN</div>"""

js = js.replace(target, replace)

with open("static/js/app.js", "w") as f:
    f.write(js)

print("app.js raw stats patched")
