import re

with open("static/js/app.js", "r") as f:
    js = f.read()

patch = """  els.auction.slotsFilled.innerText = state.myTeam.length;
  els.auction.osFilled.innerText = osCount;
  
  // Calculate Avg SR and Econ
  let totalSR = 0, srCount = 0;
  let totalEcon = 0, econCount = 0;
  
  state.myTeam.forEach(p => {
      let sr = parseFloat(p.strike_rate || 0);
      let econ = parseFloat(p.economy || 0);
      
      if (['Batsman', 'Wicket-Keeper', 'All-Rounder'].includes(p.role) && sr > 0) {
          totalSR += sr;
          srCount++;
      }
      if (['Bowler', 'All-Rounder'].includes(p.role) && econ > 0) {
          totalEcon += econ;
          econCount++;
      }
  });
  
  let avgSR = srCount > 0 ? (totalSR / srCount).toFixed(1) : "0.0";
  let avgEcon = econCount > 0 ? (totalEcon / econCount).toFixed(2) : "0.0";
  
  const srEl = document.getElementById('team-sr-display');
  const econEl = document.getElementById('team-econ-display');
  
  if (srEl) {
      srEl.innerText = avgSR;
      srEl.style.color = (parseFloat(avgSR) >= 133.0) ? 'var(--success-green)' : (avgSR === "0.0" ? 'white' : 'var(--danger-red)');
  }
  if (econEl) {
      econEl.innerText = avgEcon;
      econEl.style.color = (parseFloat(avgEcon) <= 8.00 && econCount > 0) ? 'var(--success-green)' : (avgEcon === "0.0" ? 'white' : 'var(--danger-red)');
  }
}"""

js = js.replace("""  els.auction.slotsFilled.innerText = state.myTeam.length;
  els.auction.osFilled.innerText = osCount;
}""", patch)

with open("static/js/app.js", "w") as f:
    f.write(js)
