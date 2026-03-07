from page_frame import page_frame
from list_decks_page import list_decks_page
from card_page import card_page
import tkinter as tk 

def new_page(collection, outer, type, next):
    if next and outer.count >= len(collection):
        return
    elif not next and outer.count <=0:
        return
    if outer.p_frame is not None:
            outer.p_frame.destroy()
            outer.p_frame = None
    outer.p_frame = page_frame(outer)
    if next:
        display_up_to = 9 + outer.count
        if display_up_to > len(collection):
            display_up_to = len(collection)
        outer.count_label.config(text=f"Displaying {outer.count} - {display_up_to} of {len(collection)+1}")
        for i in range(outer.count, display_up_to):
            item = collection[i]
            display(type, item, outer.p_frame, i)
        outer.count += (display_up_to - outer.count)
        if outer.count > len(collection):
            outer.count = len(collection)
    else:
        display_up_to =  outer.count - 9
        if display_up_to < 0:
            display_up_to = 0
        outer.count_label.config(text=f"Displaying {display_up_to} - {outer.count} of {len(collection)+1}")
        for i in range(display_up_to, outer.count):
            item = collection[i]
            display(type, item, outer.p_frame, i)
        outer.count -= (outer.count - display_up_to)
        if outer.count < 0:
            outer.count = 0
    outer.p_frame.grid(sticky="nsew", row=1)
    outer.outer.update_idletasks()



def display(type, item, p_frame, ind):
     match type:
        case "cards":
            x = ind%3
            y = ind//3
            frame = card_page(item, p_frame)
            frame.grid(column=x, row=y)
        case "decks":
            x = ind%3
            y = ind//3
            frame = list_decks_page(item, p_frame)
            frame.grid(column=x, row=y)





