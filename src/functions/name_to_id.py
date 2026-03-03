def name_to_id(name, collection):
    for card in collection:
        if name.upper() in card["name"].upper():
            return card["id"]
    else:
        return None