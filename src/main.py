import os, json
from functions.simplify_data import simplify_data
from functions.add_card import add_card

def main():
    non_collection = []
    if os.path.isfile("/data/non_collection.json"):
        with open("/data/non_collection.json")as f:
            non_collection = json.load(f)
    else:     
        #script to download from scryfall
        non_collection = simplify_data("data/scryfall.json")
    collection = []

    add_card()


if __name__ == "__main__":
    main()
