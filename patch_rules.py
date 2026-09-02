import re

with open("static/index.html", "r") as f:
    html = f.read()

rules_html = """      </div>

      <div class="game-rules-card glass-card" style="margin: 1.5rem 0; padding: 1.2rem; text-align: left; background: rgba(30, 41, 59, 0.7); border-left: 4px solid var(--primary-gold);">
        <h3 style="margin-top: 0; margin-bottom: 0.8rem; color: var(--primary-gold); font-size: 1rem; text-transform: uppercase; letter-spacing: 1px;">🏆 How to Win</h3>
        <ul style="padding-left: 1.2rem; margin-bottom: 0; font-size: 0.85rem; color: #cbd5e1; line-height: 1.5;">
          <li style="margin-bottom: 0.4rem;"><strong>Perfect 15:</strong> Exactly 5 Batsmen, 4 All-Rounders, 4 Bowlers, and 2 Wicket Keepers (Max 6 Overseas).</li>
          <li style="margin-bottom: 0.4rem;"><strong>Budget:</strong> You have 120 CR. Once you run out, you cannot bid!</li>
          <li><strong>Victory Condition:</strong> The AI scores your team out of 10. To win, draft players with the <strong>most total runs</strong> and <strong>most total wickets</strong>!</li>
        </ul>
      </div>

      <div class="lobby-players-section">"""

html = html.replace('      </div>\n\n      <div class="lobby-players-section">', rules_html)

with open("static/index.html", "w") as f:
    f.write(html)
