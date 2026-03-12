import tkinter as tk
from functions.new_page import new_page
from functions.search_enter import search_enter
from functions.validate_entry import validate_entry
from functions.choose_collection import choose_collection
from functions.reset_filters import reset_filters
from functions.validate_color_entry import validate_color_entry
from functions.add_cards_from_pages import add_cards_from_pages

class collection_frame(tk.Frame):
    def __init__(self, outer, root, collection):
        super().__init__(root)
        self.outer = outer
        self.collection = collection
        self.root = root
        self.count = 0
        self.p_frame = None
        self.temp_collection = None        
        
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(sticky='n')

        home = tk.Button(self.top_frame, text="Home", command=lambda: outer.set_frame("home"))        
        search_label = tk.Label(self.top_frame, text="Search by Card Name")
        search_textbox_label = tk.Label(self.top_frame, text="Search by Card Text")
        search_entry = tk.Entry(self.top_frame)        
        search_textbox_entry = tk.Entry(self.top_frame)

        cmc_filter = tk.IntVar()     
        cmc_filter.set(0)   
        vcmd = (root.register(validate_entry))
        cmc_label = tk.Label(self.top_frame, text="Filter by mana cost")
        cmc_filter_value = tk.Entry(self.top_frame, validate="key", validatecommand=(vcmd, '%P'))
        greater_than_button = tk.Radiobutton(self.top_frame, text="mana value > x", variable=cmc_filter, value=2)
        less_than_button = tk.Radiobutton(self.top_frame, text="mana value < x", variable=cmc_filter, value=-1)
        equal_to_button = tk.Radiobutton(self.top_frame, text="mana value = x", variable=cmc_filter, value=1)
        no_button = tk.Radiobutton(self.top_frame, text="no mana filter", variable=cmc_filter, value=0)

        search_button = tk.Button(self.top_frame, text="Search", command=lambda: search_enter(self.collection, search_entry.get(), (cmc_filter.get(), cmc_filter_value.get()), color_entry.get(), keywords_choice.curselection(), keywords_choice, self))
        reset_filters_button = tk.Button(self.top_frame, text="Reset Filters", command=lambda: reset_filters(search_entry, search_textbox_entry, (cmc_filter, cmc_filter_value), color_entry, keywords_choice, self.collection, self, "cards"))

        previous_button = tk.Button(self.top_frame, text="Previous", command=lambda: choose_collection(self.temp_collection, self.collection, self, "cards", False))
        self.count_label = tk.Label(self.top_frame, text=f"Displaying {self.count} - {self.count+9} of {len(self.collection)}")
        next_button = tk.Button(self.top_frame, text="Next", command=lambda: choose_collection(self.temp_collection, self.collection, self, "cards", True))

        keywords_label = tk.Label(self.top_frame, text="Keywords")
        keywords = []
        with open("keywords.txt") as f:
            text = f.read()
            keywords = text.split('\n')
        listbox_items = tk.StringVar(value=keywords)
        vcmd_color =(root.register(validate_color_entry))
        keywords_choice = tk.Listbox(self.top_frame, selectmode="multiple",listvariable=listbox_items,height=10)

        color_label = tk.Label(self.top_frame, text="Color Identity: input combination of 'wubrg'\n (or c for colorless)")
        color_entry = tk.Entry(self.top_frame, validate="key", validatecommand=(vcmd_color, '%P'))

        home.grid(row=0, column=0)
        search_label.grid(row=0, column=1)
        search_entry.grid(row=0, column=2)
        search_textbox_label.grid(row=1, column=1)
        search_textbox_entry.grid(row=1, column=2)

        search_button.grid(row=2, column=3)
        reset_filters_button.grid(row=2, column=4)

        cmc_label.grid(row=0, column=3)
        cmc_filter_value.grid(row=0, column=4)
        no_button.grid(row=0, column=5)
        greater_than_button.grid(row=1, column=5)
        less_than_button.grid(row=2, column=5)
        equal_to_button.grid(row=3, column=5)

        keywords_label.grid(row=0, column=8)
        keywords_choice.grid(row=1,column=8, rowspan=7, columnspan=7)

        color_label.grid(row=1, column=6)
        color_entry.grid(row=0, column=6) 

        previous_button.grid(row=4, column=1)
        self.count_label.grid(row=4, column=3)
        next_button.grid(row=4, column=5)

        self.add_frame = tk.Frame(self)
        self.add_frame.grid(row=3,column=0)

        add_to_collection_var = tk.IntVar()
        add_to_collection = tk.Checkbutton(self.add_frame, text="Add to Collection", onvalue=1, offvalue=0, variable=add_to_collection_var)
        deck_name_label = tk.Label(self.add_frame, text="Enter Deck Name")
        deck_name_entry = tk.Entry(self.add_frame)
        add_cards = tk.Button(self.add_frame, text="Add Cards", command=lambda: add_cards_from_pages(outer, self.p_frame, (add_to_collection_var.get(), deck_name_entry.get())))

        add_to_collection.grid(row=3,column=4) 
        deck_name_label.grid(row=3, column=2)
        deck_name_entry.grid(row=3, column=3)
        add_cards.grid(row=3, column=6)

        new_page(self.collection, self, "cards", True)      








 
