import unittest, json
from functions.name_to_id import name_to_id

class TestNameToID(unittest.TestCase):
    def test_name_to_id(self):
        commander_legal_cards = [
        {"id": "036ef8c9-72ac-46ce-af07-83b79d736538","name": "Storm Crow","cardtype": ["Creature"],"supertype": [],"subtype": ["Bird"],"color_id": ["U"],"cmc": 2.0,"cost": "{1}{U}","textbox": "Flying (This creature can't be blocked except by creatures with flying or reach.)","keywords": ["Flying"],"power": "1","toughness": "2"},
        {"id": "b125d1e7-5d9b-4997-88b0-71bdfc19c6f2","name": "Walking Sponge","cardtype": ["Creature"],"supertype": [],"subtype": ["Sponge"],"color_id": ["U"],"cmc": 2.0,"cost": "{1}{U}","textbox": "{T}: Target creature loses your choice of flying, first strike, or trample until end of turn.","keywords": [],"power": "1","toughness": "1"},
        {"id": "e0f83824-43c6-4101-88fd-9109958b23e2","name": "Ravnica at War","cardtype": ["Sorcery"],"supertype": [],"subtype": [],"color_id": ["W"],"cmc": 4.0,"cost": "{3}{W}","textbox": "Exile all multicolored permanents.","keywords": []},
        {"card_faces": [{"name": "Urabrask","cardtype": ["Creature"],"supertype": ["Legendary"],"subtype": ["Phyrexian","Praetor"],"cost": "{2}{R}{R}","textbox": "First strike\nWhenever you cast an instant or sorcery spell, Urabrask deals 1 damage to target opponent. Add {R}.\n{R}: Exile Urabrask, then return it to the battlefield transformed under its owner's control. Activate only as a sorcery and only if you've cast three or more instant and/or sorcery spells this turn.","power": "4","toughness": "4"},
        {"name": "The Great Work","cardtype": ["Enchantment"],"supertype": [],"subtype": ["Saga"],"cost": "","textbox": "(As this Saga enters and after your draw step, add a lore counter.)\nI \u2014 This Saga deals 3 damage to target opponent and each creature they control.\nII \u2014 Create three Treasure tokens.\nIII \u2014 Until end of turn, you may cast instant and sorcery spells from any graveyard. If a spell cast this way would be put into a graveyard, exile it instead. Exile this Saga, then return it to the battlefield (front face up)."}],
        "id": "712fb9e5-bd67-4173-a2d4-061aeb6253b5","name": "Urabrask // The Great Work","cardtype": ["Creature"],"supertype": ["Legendary"],"subtype": [],"color_id": ["R"],"cmc": 4.0,"keywords": ["Transform","First strike","Treasure"]},
        ]
        collection = []
        test = name_to_id("Storm Crow", commander_legal_cards)
        self.assertEqual("036ef8c9-72ac-46ce-af07-83b79d736538", test)
        test = name_to_id("Urabrask // The Great Work", commander_legal_cards)
        self.assertEqual("712fb9e5-bd67-4173-a2d4-061aeb6253b5", test)




