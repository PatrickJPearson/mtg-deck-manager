import json

def save_changes(collection, path):
    with open(path, "w") as f:
        json.dump(collection, f, indent=4)
