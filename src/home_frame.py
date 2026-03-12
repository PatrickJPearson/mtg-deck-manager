import tkinter as tk

class home_frame(tk.Frame):
    def __init__(self, outer, root):
        super().__init__(root)
        self.outer = outer
        title = tk.Label(self, text="MTG Collection Manager")
        title.grid()
        collection = tk.Button(self, text="Collection", command=lambda: outer.set_frame("collection"))
        commander_legal_cards = tk.Button(self, text="Commander Legal Cards", command=lambda: outer.set_frame("commander_legal_cards"))
        list_decks = tk.Button(self, text="Decks", command=lambda: outer.set_frame("list_decks"))
        quit = tk.Button(self, text="Quit", command=lambda: outer.set_frame("quit"))
        title.grid(row=0, column=0)
        collection.grid(row=4, column=6)
        commander_legal_cards.grid(row=5, column=6)
        list_decks.grid(row=6, column=6)
        quit.grid(row=7, column=6)




