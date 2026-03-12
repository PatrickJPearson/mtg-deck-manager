from functions.new_page import new_page

def search_enter(collection, input, mana, color, indecies, listbox, outer):
    results = []
    if input == None and mana == None:
        outer.temp_collection = None
        return
    for i in collection:
        add = True
        if ("name" in i and input.upper() in i["name"].upper()) or input == "":
            pass
        else:
            add = False
        if add and filter_mana(i, mana):
            pass
        else:
            add=False
        if add and filter_color(i, color):
            pass
        else:
            add=False
            
        keywords=[]
        for ind in indecies:
            keywords.append(listbox.get(ind))
        if add and filter_keywords(i, keywords):
            pass
        else:
            add =False
        if add:
            results.append(i)
    outer.temp_collection = results
    outer.count = 0
    new_page(results,outer,"cards",True)


def filter_mana(i, mana):
    if "cmc" not in i:
        return False
    if mana[1] == '':
        return True
    actual = i["cmc"]
    if mana[0] == 0:
        return True
    elif mana[0] ==-1:
        return actual < int(mana[1])
    elif mana[0] ==1:
        return actual == int(mana[1])
    elif mana[0] ==2:
        return actual > int(mana[1])
    
def filter_color(i, color):
    if "color_id" not in i:
        return False
    if color == '':
        return True
    for c in color:
        if not c.upper() in i["color_id"]:
            return False
    return True

def filter_keywords(i, keywords):
    if not "keywords" in i:
        return False
    if keywords == []:
        return True
    for keyword in keywords:
        if not keyword in i["keywords"]:
            return False
    return True
