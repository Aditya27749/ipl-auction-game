import re

with open("static/js/app.js", "r") as f:
    js = f.read()

# Add switch case for secret_mission
switch_case = """    case 'secret_mission':
      const card = document.getElementById('secret-mission-card');
      if (card) {
          card.style.display = 'block';
          document.getElementById('my-franchise-name').innerText = msg.ipl_team;
          document.getElementById('my-secret-captain').innerText = msg.secret_captain;
      }
      showToast(`🕵️ SECRET MISSION: You are ${msg.ipl_team}. Draft ${msg.secret_captain} for a +0.5 score bonus!`, 'success', 8000);
      break;
    case 'new_player':"""

js = js.replace("    case 'new_player':", switch_case)

with open("static/js/app.js", "w") as f:
    f.write(js)
