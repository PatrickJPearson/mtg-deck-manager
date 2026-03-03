import json

def format_deck_list(source, dest):        
    deck_list = []
    with open(source) as f:
        text = f.read()
        lines= text.split("\n")
        for line in lines:
            fields = line.split(" ", 1)
            temp = {"name":fields[1], "number":fields[0], "add_to_collection":True}
            deck_list.append(temp)
    with open(dest, 'w') as f:
        json.dump(deck_list, f)

    