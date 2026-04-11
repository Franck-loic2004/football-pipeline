from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4/"
DB_PATH = "football.db"


COMPETITIONS = ["FL1", "CL", "PL", "BL1", "SA","PD"]  # Ligue 1, Champions League, Premier League, Bundesliga, Serie A, Primera Division
HEADERS = { 'X-Auth-Token': API_KEY }

TEAMS = ["524", "81","5","109","64"]  # PSG, Barcelona, juventus, Bayern, Liverpool

PLAYER_IDS = ["3373"]  # Ousmane Dembélé, Kylian Mbappé 3373 plus tard
