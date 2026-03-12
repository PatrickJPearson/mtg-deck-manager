import tkinter as tk
from functions.new_page import new_page

class list_decks_frame(tk.Frame):
    def __init__(self, outer, root, decks):
        super().__init__(root)
        self.outer = outer
        self.count =0
        self.p_frame = None
        self.decks = decks
        self.top_frame = tk.Frame(self)    
        self.count_label = tk.Label(self.top_frame, text=f"Displaying {self.count} - {self.count+9} of {len(outer.collection)+1}")
        self.count_label.grid(row=3, column=3)        
        home = tk.Button(self.top_frame, text="Home", command=lambda: outer.set_frame("home"))
        home.grid(row=3, column=0)
        self.top_frame.grid(sticky="n")
        if decks != []:
            new_page(decks, self, "decks", True)
