import tkinter as tk
from functions.new_page import new_page
import os

class list_decks_frame(tk.Frame):
    def __init__(self, outer, root):
        super().__init__(root)
        self.outer = outer
        self.count =0
        self.p_frame = None
        self.top_frame = tk.Frame(self)    
        self.count_label = tk.Label(self.top_frame, text=f"Displaying {self.count} - {self.count+9} of {len(outer.collection)+1}")
        self.count_label.grid(row=3, column=3)        
        home = tk.Button(self.top_frame, text="Home", command=lambda: outer.setFrame("home"))
        home.grid(row=3, column=0)
        search_label = tk.Label(self.top_frame, text="Search")
        search_entry = tk.Entry(self.top_frame)
        search_label.grid(row=0, column=0)
        search_entry.grid(row=1, column=0)

        filters_label = tk.Label(self.top_frame, text="Filters")
        group_label = tk.Label(self.top_frame, text="Group")
        color_label = tk.Label(self.top_frame, text="Color")
        filters_label.grid(row=0, column=1)
        group_label.grid(row=0, column=2)
        color_label.grid(row=1, column=2)

        group_entry = tk.Entry(self.top_frame)
        color_entry = tk.Entry(self.top_frame)
        group_entry.grid(row=0, column=3)
        color_entry.grid(row=1, column=3)

        size_label = tk.Label(self.top_frame)
        is_complete = tk.IntVar()
        complete_button = tk.Radiobutton(self.top_frame, text="100 or more cards", variable=is_complete, value=True)
        incomplete_button = tk.Radiobutton(self.top_frame, text="Less than 100 cards", variable=is_complete, value=False)
        size_label.grid(row=0, column=4)
        complete_button.grid(row=0, column=5)
        incomplete_button.grid(row=1, column=5)
        self.top_frame.grid(sticky="n")
        list_decks = os.listdir("data/decks")
        deck_collection = []
        for deck in list_decks:
            path = f"data/decks/{deck}"
            if os.path.isfile(path) and not "test" in deck:
                deck_collection.append(path)
        new_page(deck_collection, self, "decks", True)
