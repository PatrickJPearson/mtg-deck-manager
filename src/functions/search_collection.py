def search_collection(collection, id, outer=None):
    for c in collection:
        if "id" in c and id == c["id"]:
            return c
    if outer:
        for c in outer:
            if id == c["id"]:
                return c
    return None