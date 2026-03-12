import functions.new_page

def view_deck(outer, deck):
    control = outer.outer
    control.set_frame("collection")
    control.c_frame.temp_collection = deck[1:]
    control.root.title(f"{deck[0]["name"]}")
    control.c_frame.count = 0
    functions.new_page.new_page(control.c_frame.temp_collection, control.c_frame, "cards", True)




