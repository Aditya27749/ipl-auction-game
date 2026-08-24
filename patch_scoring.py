with open("game_engine.py", "r") as f:
    lines = f.readlines()

out = []
skip = False
for line in lines:
    if "def calculate_team_scores" in line:
        skip = True
        new_logic = """    def calculate_team_scores(self, team: List[dict], remaining_budget: float) -> float:
        \"\"\"Advanced AI-Predictor algorithm for team points.\"\"\"
        if not team:
            return 0.0
            
        score = 0.0
        roles = {'Batsman': 0, 'Bowler': 0, 'All-Rounder': 0, 'Wicket-Keeper': 0}
        total_rating = 0.0
        overseas_count = 0
        total_runs = 0
        total_wickets = 0
        
        for p in team:
            role = p.get('role', 'Batsman')
            if role in roles:
                roles[role] += 1
            else:
                roles['Batsman'] += 1
                
            total_rating += p.get('rating', 5.0)
            if p.get('nationality', '').lower() != 'indian':
                overseas_count += 1
                
            total_runs += p.get('runs', 0)
            total_wickets += p.get('wickets', 0)

        # 1. Base Structure (Max 25 Points)
        # Ideal: 5 BAT, 4 BWL, 4 AR, 2 WK
        bat_penalty = abs(5 - roles.get('Batsman', 0)) * 2
        bwl_penalty = abs(4 - roles.get('Bowler', 0)) * 2
        ar_penalty = abs(4 - roles.get('All-Rounder', 0)) * 2
        wk_penalty = abs(2 - roles.get('Wicket-Keeper', 0)) * 3
        
        structure_score = 25 - (bat_penalty + bwl_penalty + ar_penalty + wk_penalty)
        score += max(0, structure_score)
        
        # Penalty for empty squad slots (Must be 15)
        missing_players = 15 - len(team)
        score -= (missing_players * 3)

        # 2. Overseas Limits (Max 5 Points)
        if overseas_count <= 6:
            score += 5
        else:
            score -= (overseas_count - 6) * 5

        # 3. True Statistical AI Predictor (Max 50 Points)
        # Using real Cricsheet data to predict match-winning potential
        # An elite squad (e.g. Kohli, Rohit, Bumrah) will have ~25,000 runs and ~800 wickets combined
        expected_championship_runs = 25000.0
        expected_championship_wickets = 800.0
        
        runs_points = min(25.0, (total_runs / expected_championship_runs) * 25.0)
        wickets_points = min(25.0, (total_wickets / expected_championship_wickets) * 25.0)
        
        score += runs_points
        score += wickets_points

        # 4. Star Power & Rating Synergy (Max 20 Points)
        # Captures intangible factors (strike rate aura, captaincy, etc.)
        avg_rating = total_rating / len(team)
        rating_points = (avg_rating / 10.0) * 20.0
        score += rating_points

        # Format cleanly out of 100
        final_score = round(max(0.0, min(100.0, score)), 1)
        return final_score
"""
        out.append(new_logic)
        
    if skip and "return round" in line:
        skip = False
        continue
        
    if not skip:
        out.append(line)

with open("game_engine.py", "w") as f:
    f.writelines(out)
