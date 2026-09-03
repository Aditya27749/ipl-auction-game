import re
with open("static/index.html", "r") as f:
    html = f.read()

patch = """          <div class="team-stats-row">
            <span>Slots: <strong><span id="slots-filled">0</span>/15</strong></span>
            <span>Overseas: <strong><span id="overseas-filled">0</span>/6</strong></span>
          </div>
          <div id="secret-mission-card" style="margin-top: 15px; padding: 10px; background: rgba(0, 212, 255, 0.1); border-left: 3px solid #00d4ff; border-radius: 4px; display: none;">
            <div style="font-size: 0.75rem; color: #00d4ff; font-weight: bold; text-transform: uppercase;">Your Franchise</div>
            <div id="my-franchise-name" style="font-size: 1rem; font-weight: bold; margin-bottom: 8px; color: white;">CSK</div>
            <div style="font-size: 0.75rem; color: #ffab40; font-weight: bold; text-transform: uppercase;">🎯 Secret Target (+0.5 Pts)</div>
            <div id="my-secret-captain" style="font-size: 0.9rem; font-weight: bold; color: white;">MS Dhoni</div>
          </div>"""

html = html.replace(
    """          <div class="team-stats-row">
            <span>Slots: <strong><span id="slots-filled">0</span>/15</strong></span>
            <span>Overseas: <strong><span id="overseas-filled">0</span>/6</strong></span>
          </div>""",
    patch
)

with open("static/index.html", "w") as f:
    f.write(html)
