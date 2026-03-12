import requests, json

def fetch_from_scryfall(path):
    response = requests.get("https://data.scryfall.io/oracle-cards/oracle-cards-20260312090223.json")
    data = response.json()
    with open(path, 'w') as f:
        json.dump(data, f)