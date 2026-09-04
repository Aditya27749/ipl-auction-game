import re
with open("static/index.html", "r") as f:
    html = f.read()

patch = """          <div class="team-stats-row">
            <span>Slots: <strong><span id="slots-filled">0</span>/15</strong></span>
            <span>Overseas: <strong><span id="overseas-filled">0</span>/6</strong></span>
          </div>
          <div class="team-stats-row" style="margin-top: 5px;">
            <span>Avg SR: <strong><span id="team-sr-display">0.0</span></strong></span>
            <span>Avg Econ: <strong><span id="team-econ-display">0.0</span></strong></span>
          </div>"""

html = html.replace(
    """          <div class="team-stats-row">
            <span>Slots: <strong><span id="slots-filled">0</span>/15</strong></span>
            <span>Overseas: <strong><span id="overseas-filled">0</span>/6</strong></span>
          </div>""",
    patch
)

# Also update How to Win
rule_patch = """          <li style="margin-bottom: 0.4rem;"><strong>Budget:</strong> You have 120 CR. Once you run out, you cannot bid!</li>
          <li style="margin-bottom: 0.4rem;"><strong>Stats Target:</strong> Maintain an Average Strike Rate <strong>>= 133.0</strong> and Economy <strong><= 8.00</strong> or face a huge penalty!</li>"""

html = html.replace(
    """          <li style="margin-bottom: 0.4rem;"><strong>Budget:</strong> You have 120 CR. Once you run out, you cannot bid!</li>""",
    rule_patch
)

with open("static/index.html", "w") as f:
    f.write(html)
