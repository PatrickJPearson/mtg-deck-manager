from functions.search_collection import search_collection
from functions.save_changes import save_changes
import copy

def deck_add_card(id, deck, collection, commander_legal_cards, path, number=1):
    if number == 0:
        return deck
    search = None
    if deck:
        search = search_collection(deck, id)
    if search:
            num_in_deck = int(search["number_in_deck"])
            search["number_in_deck"] = num_in_deck+ int(number)
    else:
        search = search_collection(collection, id, outer=commander_legal_cards)
        if search:
            new_card = copy.deepcopy(search)
            new_card["number_in_deck"] = number
            deck.append(new_card)
        else:
             raise Exception("Error: card does not exist or is not legal in commander")
    save_changes(deck, path)
    return collection