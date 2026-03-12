import tkinter as tk
from functions.get_deck_colors import get_deck_colors
from functions.view_deck import view_deck

class list_decks_page(tk.Frame):
    def __init__(self, deck, p_frame, outer):
            super().__init__(p_frame)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.name = tk.Label(self, text=f"Deck Name: {deck[0]["name"]}")
            self.size = tk.Label(self, text=f"Size: {deck[0]["size"]} Cards")
            self.colors = tk.Label(self, text=f"Colors: {get_deck_colors(deck)}")
            self.view = tk.Button(self, text="View Deck", command=lambda: view_deck(outer, deck))
            self.name.pack() 
            self.size.pack()
            self.colors.pack()
            self.view.pack()


