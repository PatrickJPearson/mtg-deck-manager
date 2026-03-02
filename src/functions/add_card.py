from functions.search_collection import search_collection
from functions.save_changes import save_changes
import copy

def add_card(id, collection, non_collection, path, number=1, is_deck=False):
    if number == 0:
        return collection
    search = search_collection(collection, id)
    if search:
        if is_deck:
            search["deck_quantity"] += number
        else:
            search["quantity"] += number
    else:
        search = search_collection(non_collection, id)
        if search:
            new_card = copy.deepcopy(search)
            if is_deck:
                new_card["deck_quantity"] = number
                search["number_in_decks"] = number
            else:
                new_card["quantity"] = number
                new_card["number_in_decks"] = 0
            collection.append(new_card)
        else:
            raise Exception("Error: card does not exist or is not legal in commander")
    save_changes(collection, path)
    if is_deck:
        save_changes(non_collection, "data/collection.json")
    return collection