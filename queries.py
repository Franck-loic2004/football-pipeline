import sqlite3
import pandas as pd
from config import DB_PATH

def run_queries(competition,team):

    print(f"\n{'='*50}")
    print(f"  {competition.upper()}")
    print(f"{'='*50}")
    
    with sqlite3.connect(DB_PATH) as conn:
        
        print(f"\n── Top 5 équipes de {competition} ──")
        df1 = pd.read_sql("""
            select team from standings where competition = ? order by points desc limit 5
        """, conn, params=(competition,))
        print(df1.to_string(index=False))
        print("\n")

        print(f"\n── Top 5 équipes avec le plus de buts marqués de {competition} ──")
        df2 = pd.read_sql(""" select team, goals_for from standings where competition = ? order by goals_for desc limit 5 """, conn, params=(competition,))
        print(df2.to_string(index=False))
        print("\n")

        print(f"\n── Top 5 matchs avec le plus de buts marqués de {competition} ──")
        df3 = pd.read_sql(""" select home_team, away_team, score_home + score_away as total_goals, date from matches where score_home is not null and score_away is not null and competition = ? order by total_goals desc limit 5 """, conn, params=(competition,))
        print(df3.to_string(index=False))
        print("\n")

        print(f"\n── Top 5 buteurs de {competition} ──")
        df4 = pd.read_sql(""" select player, team, goals from scorers where competition = ? order by goals desc limit 5 """, conn, params=(competition,))
        print(df4.to_string(index=False))
        print("\n")

        print(f"\n── Top 5 équipes avec le plus de victoires de {competition} ──")
        df6 = pd.read_sql(""" select team, won from standings where competition = ? order by won desc limit 5 """, conn, params=(competition,))
        print(df6.to_string(index=False))
        print("\n")

        print("\n── Derniers matchs de Dembélé ──")
        df8 = pd.read_sql("""
            SELECT date, home_team, away_team, score_home, score_away
            FROM players_matches
            WHERE status = 'FINISHED'
            ORDER BY date DESC
            LIMIT 5
        """, conn)
        print(df8.to_string(index=False))
        print("\n")


        if team:
            print(f"\n── Joueurs français de {team} ──")
            df5 = pd.read_sql("""
                SELECT player_name FROM squad 
                WHERE team = ? AND nationality = 'France'
                ORDER BY player_name
            """, conn, params=(team,))
            print(df5.to_string(index=False))
            print("\n")

        


        if team:
            print(f"\n── Les 5 prochains matchs de {team} ──")
            df7 = pd.read_sql("""
            SELECT date, home_team, away_team, stage FROM matches 
            WHERE (home_team = ? OR away_team = ?)
            AND status != 'FINISHED'
            AND competition = ?
            ORDER BY date ASC
                LIMIT 5
                """, conn, params=(team, team, competition))
            print(df7.to_string(index=False))
            print("\n")


        
    
        

        
        

        


if __name__ == "__main__":
   #   run_queries("UEFA Champions League")
    run_queries("Ligue 1", "Paris Saint-Germain FC")