with open("static/index.html", "r") as f:
    html = f.read()

import re
html = re.sub(r'      </div>\n      <div class="topbar-right".*?</div>\n\n        </div>\n      </div>',
              r'      </div>\n      <div class="topbar-right" style="margin-left: 20px;">\n        <button id="btn-destroy-game" class="btn btn-danger hidden" style="font-size: 0.8rem; padding: 0.4rem 0.8rem; background: var(--danger-red);">EXIT</button>\n      </div>', html, flags=re.DOTALL)

with open("static/index.html", "w") as f:
    f.write(html)
