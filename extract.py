import requests
import json
import time


from config import BASE_URL, HEADERS, COMPETITIONS, TEAMS, PLAYER_IDS

def get_standings(competition):
    time.sleep(6)
    url = BASE_URL + "competitions/" + competition + "/standings"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching standings: {e}")
        return {"error": str(e)}
    
    return data

def get_matches(competition):
    time.sleep(6)
    url = BASE_URL + "competitions/" + competition + "/matches"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching matches: {e}")
        return {"error": str(e)}
    
    return data

def get_scorers(competition):
    time.sleep(6)
    url = BASE_URL + "competitions/" + competition + "/scorers"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching scorers: {e}")
        return {"error": str(e)}
    
    return data

def get_teams_stats(team_id):
    time.sleep(6)
    url = BASE_URL + "teams/" + team_id 
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching teams: {e}")
        return {"error": str(e)}
    
    return data

def get_players_matches(player_id):
    time.sleep(6)
    url = BASE_URL + "persons/" + player_id + "/matches?limit=5"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching players: {e}")
        return {"error": str(e)}
    
    return data
# if __name__ == "__main__":
#     for competition in COMPETITIONS:
#         standings = get_standings(competition)
#         matches = get_matches(competition)
#         scorers = get_scorers(competition)

#         print(json.dumps(matches, indent=2))
if __name__ == "__main__":
    teams = get_teams_stats("524")  # PSG
    players = get_players_matches("3373")  # Ousmane Dembélé

    print(json.dumps(players, indent=2))
 