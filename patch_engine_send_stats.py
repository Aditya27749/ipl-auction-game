import re

with open("game_engine.py", "r") as f:
    code = f.read()

target = """                        "nationality": t.get("nationality", "Indian"),
                        "bought_price": t.get("price_paid", 0),
                        "ipl_team": t.get("ipl_team", ""),
                    })"""

replace = """                        "nationality": t.get("nationality", "Indian"),
                        "bought_price": t.get("price_paid", 0),
                        "ipl_team": t.get("ipl_team", ""),
                        "strike_rate": t.get("strike_rate", 0),
                        "economy": t.get("economy", 0),
                    })"""

code = code.replace(target, replace)

# And also for the end_auction one
target2 = """                    "nationality": t.get("nationality", "Indian"),
                    "bought_price": t.get("price_paid", 0),
                    "ipl_team": t.get("ipl_team", ""),
                    "rating": t.get("rating", 5.0),
                })"""

replace2 = """                    "nationality": t.get("nationality", "Indian"),
                    "bought_price": t.get("price_paid", 0),
                    "ipl_team": t.get("ipl_team", ""),
                    "strike_rate": t.get("strike_rate", 0),
                    "economy": t.get("economy", 0),
                    "rating": t.get("rating", 5.0),
                })"""

code = code.replace(target2, replace2)

with open("game_engine.py", "w") as f:
    f.write(code)

print("game_engine.py updated.")
