import sqlite3
import pandas as pd

from config import DB_PATH
def load_standings(df_standings):
    with sqlite3.connect(DB_PATH) as conn:
        df_standings.to_sql("standings", conn, if_exists="replace", index=False)
    

def load_matches(df_matches):
    with sqlite3.connect(DB_PATH) as conn:
        df_matches.to_sql("matches", conn, if_exists="replace", index=False)

def load_scorers(df_scorers):
    with sqlite3.connect(DB_PATH) as conn:
        df_scorers.to_sql("scorers", conn, if_exists="replace", index=False)

def load_team_squad(df_squad):
    with sqlite3.connect(DB_PATH) as conn:
        df_squad.to_sql("squad", conn, if_exists="replace", index=False)

def load_players(df_players):
    with sqlite3.connect(DB_PATH) as conn:
        df_players.to_sql("players_matches", conn, if_exists="replace", index=False)


# with sqlite3.connect(DB_PATH) as conn:
   #  tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn) 
 #    print(tables)



