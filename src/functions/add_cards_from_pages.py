from functions.add_card_list import add_card_list
from functions.add_deck import add_deck

def add_cards_from_pages(outer, p_frame, mode):
    card_list = []
    deck_name = mode[1]
    deck = None        
    if mode[0]:
        for element in p_frame.elements:
            var_name = element.add_button['variable']
            is_add = outer.root.getvar(var_name)
            if is_add:
                card_list.append({"name":element.full_name["text"], "number":1, "add_to_collection":True})
    else:
        for element in p_frame.elements:
            var_name = element.add_button['variable']
            is_add = outer.root.getvar(var_name)
            if is_add:
                card_list.append({"name":element.full_name["text"], "number":1, "add_to_collection":False})
    if deck_name is not None and mode[1]:
        for item in outer.decks:
            if item[0]["name"] == deck_name:
                deck = item   
        deck_path = f"data/decks/{deck_name}.json"
        if deck == None:
            add_deck(deck_name, outer, card_list)
        else:
            add_card_list(card_list, outer.collection, outer.commander_legal_cards, outer.collection_path, deck_path=deck_path, deck=deck)
    else:
        if mode[0]:
            add_card_list(card_list, outer.collection, outer.commander_legal_cards, outer.collection_path)


