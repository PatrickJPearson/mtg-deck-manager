import tkinter as tk
import page_frame
from functions.new_page import new_page

class collection_frame(tk.Frame):
    def __init__(self, outer, root):
        super().__init__(root)
        self.outer = outer
        self.root = root
        self.count = 0
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(sticky='n')
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
        greater_than_button = tk.Radiobutton(self.top_frame, text="mana value > x", variable=is_complete, value=True)
        less_than_button = tk.Radiobutton(self.top_frame, text="mana value < x", variable=is_complete, value=False)
        size_label.grid(row=0, column=4)
        greater_than_button.grid(row=0, column=5)
        less_than_button.grid(row=1, column=5)

        previous_button = tk.Button(self.top_frame, text="Previous", command=lambda: new_page(self.outer.collection, self, "cards", False))
        next_button = tk.Button(self.top_frame, text="Next", command=lambda: new_page(self.outer.collection, self, "cards", True))

        previous_button.grid(column=4, row=3)
        next_button.grid(column=9, row=3)

        self.p_frame = None
        new_page(outer.collection, self, "cards", True)








 
