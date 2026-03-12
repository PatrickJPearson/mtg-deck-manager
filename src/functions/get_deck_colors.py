def get_deck_colors(deck):
    color_set = set()
    for card in deck:
        if "color_id" in card:
            for color in card["color_id"]:
                color_set.add(color)
    return color_set