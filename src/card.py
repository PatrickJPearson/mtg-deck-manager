from enum import Enum

class card():
    def __init__(self, dict):
        self.dict = dict
        self.quantity = 0
        self.number_in_decks = 0



class cardtype(Enum):
    CREATURE = "Creature"
    LAND = "Land"
    ARTIFACT = "Artifact"
    ENCHANTMENT = "Enchantment"
    PLANESWALKER = "Planeswalker"
    INSTANT = "Instant"
    SORCERY = "Sorcery"

class supertype(Enum):
    BASIC = "Basic"
    LEGENDARY = "Legendary"
    WORLD = "World"
    SNOW = "Snow"
