def search_collection(collection, id):
    for c in collection:
        if id == c["id"]:
            return c
    return None