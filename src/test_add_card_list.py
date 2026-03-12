import unittest
from functions.add_card_list import add_card_list

class TestAddCardList(unittest.TestCase):
    def test_add_card_list(self):
        commander_legal_cards = [
        {"id": "036ef8c9-72ac-46ce-af07-83b79d736538","name": "Storm Crow","cardtype": ["Creature"],"supertype": [],"subtype": ["Bird"],"color_id": ["U"],"cmc": 2.0,"cost": "{1}{U}","textbox": "Flying (This creature can't be blocked except by creatures with flying or reach.)","keywords": ["Flying"],"power": "1","toughness": "2"},
        {"id": "b125d1e7-5d9b-4997-88b0-71bdfc19c6f2","name": "Walking Sponge","cardtype": ["Creature"],"supertype": [],"subtype": ["Sponge"],"color_id": ["U"],"cmc": 2.0,"cost": "{1}{U}","textbox": "{T}: Target creature loses your choice of flying, first strike, or trample until end of turn.","keywords": [],"power": "1","toughness": "1"},
        {"id": "e0f83824-43c6-4101-88fd-9109958b23e2","name": "Ravnica at War","cardtype": ["Sorcery"],"supertype": [],"subtype": [],"color_id": ["W"],"cmc": 4.0,"cost": "{3}{W}","textbox": "Exile all multicolored permanents.","keywords": []},
        {"card_faces": [{"name": "Urabrask","cardtype": ["Creature"],"supertype": ["Legendary"],"subtype": ["Phyrexian","Praetor"],"cost": "{2}{R}{R}","textbox": "First strike\nWhenever you cast an instant or sorcery spell, Urabrask deals 1 damage to target opponent. Add {R}.\n{R}: Exile Urabrask, then return it to the battlefield transformed under its owner's control. Activate only as a sorcery and only if you've cast three or more instant and/or sorcery spells this turn.","power": "4","toughness": "4"},
        {"name": "The Great Work","cardtype": ["Enchantment"],"supertype": [],"subtype": ["Saga"],"cost": "","textbox": "(As this Saga enters and after your draw step, add a lore counter.)\nI \u2014 This Saga deals 3 damage to target opponent and each creature they control.\nII \u2014 Create three Treasure tokens.\nIII \u2014 Until end of turn, you may cast instant and sorcery spells from any graveyard. If a spell cast this way would be put into a graveyard, exile it instead. Exile this Saga, then return it to the battlefield (front face up)."}],
        "id": "712fb9e5-bd67-4173-a2d4-061aeb6253b5","name": "Urabrask // The Great Work","cardtype": ["Creature"],"supertype": ["Legendary"],"subtype": [],"color_id": ["R"],"cmc": 4.0,"keywords": ["Transform","First strike","Treasure"]},
        ]
        card_list = [{"name":"Storm Crow", "number":1, "add_to_collection":True}, {"name":"Walking Sponge", "number":1, "add_to_collection":True}, {"name":"Ravnica at War", "number":2, "add_to_collection":True}, {"name":"Urabrask // The Great Work", "number":1, "add_to_collection":True} ]
        collection = []
        deck = []
        test = add_card_list(card_list, collection, commander_legal_cards,"data/test_add_card_list.json", deck_path="data/decks/test_add_card_list.json", deck=deck)
        with open("data/decks/test_add_card_list.json") as f:
            test = f.read()
            self.assertTrue('"number_in_deck": 1' in test)
            self.assertTrue("Ravnica at War" in test)
        with open("data/test_add_card_list.json") as f:
            test = f.read()
            self.assertTrue("Urabrask" in test)
            self.assertTrue('"number_in_deck": 2' in test)





