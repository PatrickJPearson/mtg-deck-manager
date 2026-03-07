import os, json, tkinter as tk
import tkinter.font as tkFont
from functions.simplify_data import simplify_data
from control_frame import control_frame

def main():
    commander_legal_cards = []
    if os.path.isfile("/data/commander_legal_cards.json"):
        with open("/data/commander_legal_cards.json")as f:
            commander_legal_cards = json.load(f)
    else:     
        #script to download from scryfall
        commander_legal_cards = simplify_data("data/scryfall.json")
    collection_path = "data/scryfall.json"
    collection = []
    if os.path.isfile("data/collection.json"):
        with open("data/collection.json")as f:
            collection = json.load(f)
    else:
        with open("data/collection.json", 'w') as e:
            e.write("[]")
    root = tk.Tk()
    root.geometry("2200x1800")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=12)
    control = control_frame(root, collection, collection_path, commander_legal_cards)
    control.h_frame.tkraise()

    root.mainloop()

    


if __name__ == "__main__":
    main()
