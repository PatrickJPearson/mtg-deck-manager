-add cards to collection
    -if card not in collection/non-collection files, search scryfall
    -if found add to collection file
    -otherwise report error
-add deck of cards (precon)
-search for cards (inside collection or from scryfall)
    -when a card not saved in file is searched, search scryfall for card
    -if found add to non-collection file
    -otherwise report error
-build decks from collection/non-collection
-when searching suggest cards based on input
    -indicate whether suggested card is in collection
        -indicate whether card is in a deck



card
-image
-card type
-power
-toughness
-cost
-textbox


? oop hierarchy for card->enchantment etc


? functional
-json to card
-search collection
-search non-collection
-search scryfall
-suggest card
-create deck
-modify deck