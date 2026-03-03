from functions.search_collection import search_collection
from functions.save_changes import save_changes
import copy

def collection_add_card(id, collection, commander_legal_cards, path, number=1, number_to_decks=0):
    if number == 0:
        return collection
    search = None
    if collection:
        search = search_collection(collection, id)
    if search:
        quantity = int(search["quantity"])
        search["quantity"] = quantity + int(number)
        if number_to_decks:
            search["number_in_deck"] += number_to_decks
    else:
        if commander_legal_cards:
            search = search_collection(commander_legal_cards, id)
        if search:
            new_card = copy.deepcopy(search)
            new_card["quantity"] = number
            new_card["number_in_deck"] = number_to_decks
            collection.append(new_card)
        else:
            raise Exception("Error: card does not exist or is not legal in commander")
    save_changes(collection, path)
    return collection