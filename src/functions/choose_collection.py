from functions.new_page import new_page

def choose_collection(temp_collection, collection, outer, type, next):
    if temp_collection:
        new_page(temp_collection, outer, type, next)
    else:
        new_page(collection, outer, type, next)