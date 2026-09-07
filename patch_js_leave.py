import re

with open("static/js/app.js", "r") as f:
    js = f.read()

target = """  els.lobby.btnLeave.addEventListener('click', disconnectWs);"""
replace = """  els.lobby.btnLeave.addEventListener('click', () => {
    sendMessage({ type: 'leave_room' });
    setTimeout(() => disconnectWs(), 200);
  });"""

js = js.replace(target, replace)

with open("static/js/app.js", "w") as f:
    f.write(js)

print("app.js patched")
