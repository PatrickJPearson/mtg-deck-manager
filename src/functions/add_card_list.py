from functions.collection_add_card import collection_add_card
from functions.name_to_id import name_to_id
from functions.deck_add_card import deck_add_card

def add_card_list(card_list, collection, commander_legal_cards, collection_path, deck_path=None, deck=None):
    if card_list:
        is_add_deck = deck is not None and deck_path is not None
        for card in card_list:
            name = card["name"]
            quantity = card["number"]
            id = name_to_id(name, commander_legal_cards)
            if card["add_to_collection"]:
                if is_add_deck:
                    collection_add_card(id, collection, commander_legal_cards, collection_path, number=quantity, number_to_decks=quantity)
                else:
                    collection_add_card(id, collection, commander_legal_cards, collection_path, number=quantity)
            if is_add_deck:
                deck_add_card(id, deck, collection, commander_legal_cards, deck_path, number=quantity)  
    else:
        raise Exception("Error: no cards in list")
