import unittest, json
from functions.search_collection import search_collection

class TestSearchCollection(unittest.TestCase):
    def test_add_cards(self):
        c = [{"id": "b125d1e7-5d9b-4997-88b0-71bdfc19c6f2","name": "Walking Sponge","cardtype": ["Creature"],"supertype": [],"subtype": ["Sponge"],"color_id": ["U"],"cmc": 2.0,"cost": "{1}{U}","textbox": "{T}: Target creature loses your choice of flying, first strike, or trample until end of turn.","keywords": [],"power": "1","toughness": "1"}]
        with open("data/non-collection.json") as f:
            non_collection = json.load(f)
            search = search_collection(non_collection, "b125d1e7-5d9b-4997-88b0-71bdfc19c6f2")
            self.assertTrue(search)
            self.assertEqual(search["id"], "b125d1e7-5d9b-4997-88b0-71bdfc19c6f2")