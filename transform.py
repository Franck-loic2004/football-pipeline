import pandas as pd
from extract import get_scorers, get_matches, get_standings, get_teams_stats, get_players_matches

def transform_standings(raw_standings):
    if "standings" not in raw_standings:
        print(f"[WARN] Pas de données standings : {raw_standings.get('message', 'erreur inconnue')}")
        return pd.DataFrame()
    table = raw_standings["standings"][0]["table"]
    
    rows = []
    for team in table:
        rows.append({
            "position": team["position"],
            "team":     team["team"]["name"],
            "points":   team["points"],
            "played_games": team["playedGames"],
            "won": team["won"],
            "draw": team["draw"],
            "lost": team["lost"],
            "goals_for": team["goalsFor"],
            "goals_against": team["goalsAgainst"],
            "goal_difference": team["goalDifference"] ,
            "competition": raw_standings["competition"]["name"]
            
        })
    
    df = pd.DataFrame(rows)
    return df

def transform_matches(raw_matches):
    if "matches" not in raw_matches:
        print(f"[WARN] Pas de données matches : {raw_matches.get('message', 'erreur inconnue')}")
        return pd.DataFrame()
    matches = raw_matches["matches"]
    
    rows = []
    for match in matches:
        rows.append({
            "date": match["utcDate"],
            "home_team": match["homeTeam"]["name"] or "N/A",
            "away_team": match["awayTeam"]["name"] or "N/A",
            "status": match["status"],
            "score_home": match["score"]["fullTime"]["home"],
            "score_away": match["score"]["fullTime"]["away"],
            "stage": match["stage"],
            "competition": raw_matches["competition"]["name"]

           
        })
    
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df

def transform_scorers(raw_scorers):
    if "scorers" not in raw_scorers:
        print(f"[WARN] Pas de données scorers : {raw_scorers.get('message', 'erreur inconnue')}")
        return pd.DataFrame()
    scorers = raw_scorers["scorers"]
    
    rows = []
    for scorer in scorers:
        rows.append({
            "player": scorer["player"]["name"],
            "team": scorer["team"]["name"],
            "goals": scorer["goals"],
            "competition": raw_scorers["competition"]["name"]
        })
    
    df = pd.DataFrame(rows)
    return df



def transform_squad(raw_team):
    rows = []
    for player in raw_team["squad"]:
        rows.append({
            "team":          raw_team["name"],
            "player_name":   player["name"],
            "position":      player["position"],
            "nationality":   player["nationality"],
            "date_of_birth": player["dateOfBirth"],
        })
    return pd.DataFrame(rows)

def transform_players(raw_players):
    if "matches" not in raw_players:
        print(f"[WARN] Pas de données players : {raw_players.get('message', 'erreur inconnue')}")
        return pd.DataFrame()
    matches = raw_players["matches"]
    
    rows = []
    for match in matches:
        rows.append({
            "date": match["utcDate"],
            "home_team": match["homeTeam"]["name"] or "N/A",
            "away_team": match["awayTeam"]["name"] or "N/A",
            "status": match["status"],
            "score_home": match["score"]["fullTime"]["home"],
            "score_away": match["score"]["fullTime"]["away"],
            "stage": match["stage"]
        })
    
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df


if __name__ == "__main__":
    

    raw_standings = get_standings("CL")
    raw_matches = get_matches("CL")
    raw_scorers = get_scorers("CL")
    raw_teams = get_teams_stats("524")  # PSG
    raw_players = get_players_matches("3373")  # Ousmane Dembélé

    df_standings = transform_standings(raw_standings)
    df_matches = transform_matches(raw_matches)
    df_scorers = transform_scorers(raw_scorers)
    
    df_squad = transform_squad(raw_teams)
    df_players = transform_players(raw_players)




    print(df_standings)
    print(df_matches)
    print(df_scorers)
    
    print(df_squad)
    print(df_players)