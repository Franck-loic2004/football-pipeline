from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4/"
DB_PATH = "football.db"


COMPETITIONS = ["FL1", "CL", "PL", "BL1", "SA"]  # Ligue 1, Champions League, Premier League, Bundesliga, Serie A
HEADERS = { 'X-Auth-Token': API_KEY }
