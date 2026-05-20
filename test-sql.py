import sqlite3
import pandas as pd
from config import DB_PATH

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql("""
        SELECT s.player, s.goals, s.team, st.points, st.position
        FROM scorers s
        JOIN standings st ON s.team = st.team
        WHERE s.competition = 'UEFA Champions League'
        AND st.competition = 'UEFA Champions League'
        ORDER BY s.goals DESC
    """, conn)
    print(df)