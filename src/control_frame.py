import tkinter as tk
from home_frame import home_frame
from list_decks_frame import list_decks_frame
from collection_frame import collection_frame

class control_frame(tk.Frame):
    def __init__(self, root, collection, collection_path, commander_legal_cards):
        super().__init__(root)
        self.root = root
        self.collection = collection
        self.collection_path = collection_path
        self.commander_legal_cards = commander_legal_cards
        self.l_d_frame = list_decks_frame(self, root)
        self.c_frame = collection_frame(self, root)
        self.h_frame = home_frame(self, root)
        self.l_d_frame.grid(row=0, column=0,sticky="nsew")
        self.c_frame.grid(row=0, column=0,sticky="nsew")
        self.h_frame.grid(row=0, column=0, sticky="nsew")


    def setFrame(self, frame_name):
        match frame_name:
            case "home":
                self.h_frame.tkraise()
            case "collection":
                self.c_frame.tkraise()
            case "list_decks":
                self.l_d_frame.tkraise()
            case "quit":
                self.root.destroy()