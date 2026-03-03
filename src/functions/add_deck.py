import os, json
from functions.add_card_list import add_card_list

def add_deck(name, collection, commander_legal_cards, collection_path, deck_list=None):
    if name:
        path = f"data/decks/{name}.json"
    else:
        raise Exception("Error: invalid name")
    deck = [{"name":name,"required_size":100,"size":0}]
    if os.path.isfile(path):
        raise Exception("Error: a deck with this name already exists")
    if deck_list:
        add_card_list(deck_list, collection, commander_legal_cards, collection_path, deck_path=path, deck=deck)
    
    