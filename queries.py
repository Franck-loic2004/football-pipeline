import sqlite3
import pandas as pd
from config import DB_PATH

def run_queries(competition):

    print(f"\n{'='*50}")
    print(f"  {competition.upper()}")
    print(f"{'='*50}")
    
    with sqlite3.connect(DB_PATH) as conn:
        
        print("\n── Top 5 équipes ──")
        df1 = pd.read_sql("""
            select team from standings where competition = ? order by points desc limit 5
        """, conn, params=(competition,))
        print(df1.to_string(index=False))

        print("\n── Top 5 équipes avec le plus de buts marqués ──")
        df2 = pd.read_sql(""" select team, goals_for from standings where competition = ? order by goals_for desc limit 5 """, conn, params=(competition,))
        print(df2.to_string(index=False))

        print("\n── Top 5 matchs avec le plus de buts marqués ──")
        df3 = pd.read_sql(""" select home_team, away_team, score_home + score_away as total_goals, date from matches where score_home is not null and score_away is not null and competition = ? order by total_goals desc limit 5 """, conn, params=(competition,))
        print(df3.to_string(index=False))

        print("\n── Top 5 buteurs ──")
        df4 = pd.read_sql(""" select player, team, goals from scorers where competition = ? order by goals desc limit 5 """, conn, params=(competition,))
        print(df4.to_string(index=False))



if __name__ == "__main__":
    run_queries("UEFA Champions League")
    run_queries("Ligue 1")