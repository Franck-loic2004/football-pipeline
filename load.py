import sqlite3

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
    

