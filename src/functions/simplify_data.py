from functions.extract_types import extract_types
import json

def simplify_data(path):
    simpler = []
    with open(path) as f:
        cards = json.load(f)
        for c in cards:
            if c["legalities"]["commander"] == 'legal':
                temp ={}
                if "card_faces" in c:
                    temp["card_faces"] = [{},{}]
                temp = set_parameters("id", "id", c, temp)
                temp = set_parameters("name", "name", c, temp)
                temp = set_parameters("type_line", None, c, temp)
                temp = set_parameters("color_identity", "color_id", c, temp)
                temp = set_parameters("cmc", "cmc", c, temp)
                temp = set_parameters("mana_cost", "cost", c, temp)
                temp = set_parameters("oracle_text", "textbox", c, temp)
                temp = set_parameters("keywords", "keywords", c, temp)
                temp = set_parameters("power", "power", c, temp)
                temp = set_parameters("toughness", "toughness", c, temp)
                simpler.append(temp)
    with open("data/commander_legal_cards.json", 'w') as f:
        json.dump(simpler, f, indent=4)
    return simpler

def set_parameters(scryfall_key, my_key, card, dict):
    if scryfall_key == "type_line":
        if " // " in card[scryfall_key]:
            if scryfall_key in  card["card_faces"][0]:
                supertype, cardtype, subtype = extract_types(card["card_faces"][0][scryfall_key])
                dict["card_faces"][0]["cardtype"], dict["card_faces"][0]["supertype"], dict["card_faces"][0]["subtype"] = cardtype, supertype, subtype
            if scryfall_key in  card["card_faces"][1]:
                supertype2, cardtype2, subtype2 = extract_types(card["card_faces"][1][scryfall_key])
                dict["card_faces"][1]["cardtype"], dict["card_faces"][1]["supertype"], dict["card_faces"][1]["subtype"] = cardtype2, supertype2, subtype2
        supertype, cardtype, subtype = extract_types(card[scryfall_key].replace(" // ", ''))
        dict["cardtype"], dict["supertype"], dict["subtype"] = cardtype, supertype, subtype
    else:
        if scryfall_key in card:
            dict[my_key] = card[scryfall_key]
        if "card_faces" in card:
            if scryfall_key in card["card_faces"][0]:
                dict["card_faces"][0][my_key] = card["card_faces"][0][scryfall_key]
            if scryfall_key in card["card_faces"][1]:
                dict["card_faces"][1][my_key] = card["card_faces"][1][scryfall_key]
    return dict