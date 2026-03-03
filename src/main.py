import os, json
from functions.simplify_data import simplify_data
from functions.format_deck_list import format_deck_list
from functions.add_deck import add_deck

def main():
    commander_legal_cards = []
    if os.path.isfile("/data/commander_legal_cards.json"):
        with open("/data/commander_legal_cards.json")as f:
            commander_legal_cards = json.load(f)
    else:     
        #script to download from scryfall
        commander_legal_cards = simplify_data("data/scryfall.json")
    collection = []
    if os.path.isfile("data/collection.json"):
        with open("data/collection.json")as f:
            collection = json.load(f)
    else:
        with open("data/collection.json") as e:
            e.write("")
    #format_deck_list("data/decks/uratest.txt", "data/decks/uraburn.json")
    with open("data/decks/uraburnsource.json")as f:
        deck_list = json.load(f)
        add_deck("uraburn", collection, commander_legal_cards, "data/collection.json", deck_list=deck_list)


    


if __name__ == "__main__":
    main()
