from extract import get_matches, get_standings, get_scorers, get_teams_stats, get_players_matches
from transform import transform_matches, transform_standings, transform_scorers,  transform_squad, transform_players
from  load import load_standings, load_matches, load_scorers, load_players, load_team_squad
from queries import run_queries
from config import COMPETITIONS, TEAMS, PLAYER_IDS
import schedule
import time
import pandas as pd

def run_pipeline():
    
    all_standings = []
    all_matches = []
    all_scorers = []
    all_players = []
    all_squad = []
    


    for competition in COMPETITIONS:
        # Extraction
        print(f"[1/4] Extraction et transformation des données pour {competition}...")
        
        raw = get_standings(competition) 
        df = transform_standings(raw)
        all_standings.append(df)
   
        raw = get_matches(competition)
        df = transform_matches(raw)
        all_matches.append(df)

        raw = get_scorers(competition)
        df = transform_scorers(raw)
        all_scorers.append(df)

    for team_id in TEAMS:
        raw = get_teams_stats(team_id)
        df = transform_squad(raw)
        all_squad.append(df)   

    for player_id in PLAYER_IDS: 

        raw = get_players_matches(player_id)
        df = transform_players(raw)
        df["player_id"] = player_id
        all_players.append(df)



    # Concaténation des données
    print("[2/4] Extraction et transformation des données terminée. Concaténation des résultats...")

    df_standings = pd.concat(all_standings, ignore_index=True)
    df_matches = pd.concat(all_matches, ignore_index=True)
    df_scorers = pd.concat(all_scorers, ignore_index=True)
    df_squad = pd.concat(all_squad, ignore_index=True)
    df_players = pd.concat(all_players, ignore_index=True)
    

    # Chargement des données
    print("[3/4] Chargement des données dans la base...")
    load_standings(df_standings)
    load_matches(df_matches)
    load_scorers(df_scorers)
    load_team_squad(df_squad)
    load_players(df_players)  

    # Requêtes
    print("[4/4] Exécution des requêtes...")
    run_queries("UEFA Champions League", None)
    print("\n\n")
    run_queries("Premier League","Liverpool FC")
    print("\n\n")
    run_queries("Primera Division", "FC Barcelona")
    print("\n\n")
    run_queries("Serie A", "Juventus FC")
    print("\n\n")
    run_queries("Bundesliga", "FC Bayern München")
    print("\n\n")
    run_queries("Ligue 1", "Paris Saint-Germain FC")
    print("\n")
    
    

if __name__ == "__main__":
    run_pipeline()
    # schedule le pipeline pour s'exécuter tous les jours à 07:00
    schedule.every().day.at("07:00").do(run_pipeline)
    print("Pipeline scheduled pour s'exécuter tous les jours à 07:00.")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check toutes les minutes

