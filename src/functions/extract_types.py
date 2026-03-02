from card import supertype, cardtype

def extract_types(typeline):
    split_off_subtypes = typeline.split(" — ")
    subtypes = []
    if len(split_off_subtypes) == 2:
        subtypes.extend(split_off_subtypes[1].split(' '))
    supertypes_and_cardtypes = split_off_subtypes[0].split(' ')
    supertypes = []
    cardtypes = []
    for type in supertypes_and_cardtypes:
        if type in [member.value for member in supertype]:
            supertypes.append(type)
        elif type in [member.value for member in cardtype]:
            cardtypes.append(type)
    return supertypes, cardtypes, subtypes