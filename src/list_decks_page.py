import tkinter as tk
import json

class list_decks_page(tk.Frame):
    def __init__(self, item, p_frame):
            super().__init__(p_frame)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            with open(item) as f:
                  deck = json.load(f)
            self.name = tk.Label(self, text=f"{deck[0]["name"]}")
            self.name.grid(row=0,column=0) 


