import tkinter as tk
from home_frame import home_frame
from list_decks_frame import list_decks_frame
from collection_frame import collection_frame

class control_frame(tk.Frame):
    def __init__(self, root, collection, collection_path, commander_legal_cards, decks):
        super().__init__(root)
        self.root = root
        self.collection = collection
        self.collection_path = collection_path
        self.commander_legal_cards = commander_legal_cards
        self.decks = decks
        self.l_d_frame = list_decks_frame(self, root, decks)
        self.c_frame = collection_frame(self, root, collection)
        self.clc_frame = collection_frame(self, root, commander_legal_cards)
        self.h_frame = home_frame(self, root)
        self.deck_frame = None
        self.l_d_frame.grid(row=0, column=0,sticky="nsew")
        self.c_frame.grid(row=0, column=0,sticky="nsew")
        self.clc_frame.grid(row=0, column=0, sticky="nsew")
        self.h_frame.grid(row=0, column=0, sticky="nsew")



    def set_frame(self, frame_name):
        match frame_name:
            case "home":
                self.root.title("MTG Deck Manager")
                self.h_frame.tkraise()
            case "collection":
                self.root.title("Collection")
                self.c_frame.tkraise()
            case "list_decks":
                self.root.title("Decks")
                self.l_d_frame.tkraise()
            case "commander_legal_cards":
                self.root.title("Commander Legal Cards")
                self.clc_frame.tkraise()
            case "quit":
                self.root.destroy()
            case _:
                self.root.title(frame_name)
                self.deck_frame.tkraise()