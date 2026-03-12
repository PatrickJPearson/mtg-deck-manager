import os, json, tkinter as tk
import tkinter.font as tkFont
from functions.simplify_data import simplify_data
from control_frame import control_frame
from functions.fetch_from_scryfall import fetch_from_scryfall

def main():
    commander_legal_cards = []
    if os.path.isfile("data/commander_legal_cards.json"):
        with open("data/commander_legal_cards.json")as f:
            commander_legal_cards = json.load(f)
    else:     
        #script to download from scryfall
        fetch_from_scryfall("data/scryfall.json")
        commander_legal_cards = simplify_data("data/scryfall.json")
    collection_path = "data/commander_legal_cards.json"
    collection = []
    if os.path.isfile("data/collection.json"):
        with open("data/collection.json")as f:
            collection = json.load(f)
    else:
        with open("data/collection.json", 'w') as e:
            e.write("[]")
    decks = []
    if os.path.isdir("data/decks"):
        for item in os.listdir("data/decks"):
            path = f"data/decks/{item}"
            if os.path.isfile(path) and "test" not in item:
                with open(path) as f:
                    deck = json.load(f)
                    decks.append(deck)
    root = tk.Tk()
    root.geometry("2200x1800")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=12)
    control = control_frame(root, collection, collection_path, commander_legal_cards, decks)
    control.set_frame("home")

    root.mainloop()

    


if __name__ == "__main__":
    main()
