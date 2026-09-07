import re
with open("game_engine.py", "r") as f:
    code = f.read()

# Update end_auction caller
caller_target = """            score = self.calculate_team_scores(team, player_info["budget"], player_info.get("secret_captain"))
            update_team_score(self.room_id, user_id, score)
            
            # Normalize team for frontend"""
caller_replace = """            score_data = self.calculate_team_scores(team, player_info["budget"], player_info.get("secret_captain"))
            update_team_score(self.room_id, user_id, score_data["total"])
            
            # Normalize team for frontend"""
code = code.replace(caller_target, caller_replace)

result_target = """            results.append({
                "user_id": user_id,
                "player_name": player_info["name"],
                "score": score,
                "team": normalized_team,"""
result_replace = """            results.append({
                "user_id": user_id,
                "player_name": player_info["name"],
                "score": score_data["total"],
                "score_breakdown": score_data,
                "team": normalized_team,"""
code = code.replace(result_target, result_replace)

# Update calculate_team_scores
func_target = """        # Format cleanly out of 10
        final_score = round(max(0.0, min(10.0, score / 10.0)), 1)
        
        # Secret Captain Bonus (Can break the 10.0 limit!)
        if secret_captain:
            for p in team:
                if p["name"] == secret_captain:
                    final_score += 0.5
                    break
                    
        return final_score"""

func_replace = """        # 4. Strict Strike Rate and Economy constraints
        total_sr = 0.0
        sr_count = 0
        total_econ = 0.0
        econ_count = 0
        
        for p in team:
            role = p.get('role', 'Batsman')
            if role in ['Batsman', 'Wicket-Keeper', 'All-Rounder'] and p.get('strike_rate', 0) > 0:
                total_sr += p.get('strike_rate', 0)
                sr_count += 1
            if role in ['Bowler', 'All-Rounder'] and p.get('economy', 0) > 0:
                total_econ += p.get('economy', 0)
                econ_count += 1
                
        avg_sr = (total_sr / sr_count) if sr_count > 0 else 0.0
        avg_econ = (total_econ / econ_count) if econ_count > 0 else 99.0
        
        sr_penalty = 0.0
        econ_penalty = 0.0
        
        if avg_sr < 133.0:
            sr_penalty = -20.0
            score += sr_penalty
        
        if avg_econ > 8.0:
            econ_penalty = -20.0
            score += econ_penalty

        # Format cleanly out of 10
        final_score = round(max(0.0, min(10.0, score / 10.0)), 1)
        
        # Breakdown values scaled to /10
        structure_display = round(max(0.0, structure_score / 10.0), 2)
        overseas_display = 0.5 if overseas_count <= 6 else round(max(0.0, (5 - (overseas_count - 6) * 5) / 10.0), 2)
        runs_display = round(runs_points / 10.0, 2)
        wickets_display = round(wickets_points / 10.0, 2)
        
        # Secret Captain Bonus (Can break the 10.0 limit!)
        bonus = 0.0
        if secret_captain:
            for p in team:
                if p["name"] == secret_captain:
                    bonus = 0.5
                    final_score += bonus
                    break
                    
        return {
            "total": final_score,
            "structure": structure_display,
            "overseas": overseas_display,
            "runs": runs_display,
            "wickets": wickets_display,
            "sr_penalty": round(sr_penalty / 10.0, 1),
            "econ_penalty": round(econ_penalty / 10.0, 1),
            "bonus": bonus
        }"""

code = code.replace(func_target, func_replace)

code = code.replace("def calculate_team_scores(self, team: List[dict], remaining_budget: float, secret_captain: str = None) -> float:", "def calculate_team_scores(self, team: List[dict], remaining_budget: float, secret_captain: str = None) -> dict:")

with open("game_engine.py", "w") as f:
    f.write(code)

print("game_engine.py patched.")
