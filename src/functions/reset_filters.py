import tkinter as tk
from functions.new_page import new_page

def reset_filters(search, search_text, cmc, color, keywords, collection, outer, type):
    if outer.temp_collection != None:
        outer.temp_collection = None
        outer.count = 0
        new_page(collection, outer, type, True)
    search.delete(0, tk.END)
    search_text.delete(0, tk.END)
    cmc[0].set(0)
    cmc[1].delete(0, tk.END)
    color.delete(0, tk.END)
    keywords.selection_clear(0, tk.END)
