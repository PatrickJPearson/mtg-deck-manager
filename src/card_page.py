import tkinter as tk

class card_page(tk.Frame):
    def __init__(self, item, p_frame):
            super().__init__(p_frame)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.full_name = tk.Label(self, text=f"{item["name"]}")
            self.full_name.pack()

            if "color_id" in item and not item["color_id"] == []:
                self.color_id = tk.Label(self, text=f"color_id: {item["color_id"]}")
                self.color_id.pack()
            if "card_faces" in item and not item["card_faces"] == []:
                self.card_faces = tk.Label(self, text=f"is dual faced")
                self.card_faces.pack()
                self.build_card_page(item, True, True)

            else:
                self.build_card_page(item, False, False)



    def build_card_page(self, item, is_recursive, is_dual_faced):
        card = item
        if is_dual_faced and is_recursive:
            card = item["card_faces"][0]
        elif is_dual_faced:
            card = item["card_faces"][1]
        if "name" in card and is_dual_faced and not card == []:
            if is_recursive:
                self.name0 = tk.Label(self, text=f"Font Face: {card["name"]}")
                self.name0.pack()
            else:
                self.name = tk.Label(self, text=f"Back Face: {card["name"]}")
                self.name.pack()
        if "cost" in card and not card["cost"] == [] and not card["cost"]=="":
            if is_recursive:
                self.cost0 = tk.Label(self, text=f"Cost: {card["cost"]}")
                self.cost0.pack()
            else:
                self.cost = tk.Label(self, text=f"Cost: {card["cost"]}")
                self.cost.pack()   
        if "cmc" in card and not card["cmc"] == []:
            if is_recursive:
                self.cmc0 = tk.Label(self, text=f"Cmc: {card["cmc"]}")
                self.cmc0.pack()
            else:
                self.cmc = tk.Label(self, text=f"Cmc: {card["cmc"]}")
                self.cmc.pack()
        if "cardtype" in card and not card["cardtype"] == []:
            if is_recursive:
                self.cardtype0 = tk.Label(self, text=f"Cardtype: {card["cardtype"]}")
                self.cardtype0.pack()
            else:
                self.cardtype = tk.Label(self, text=f"Cardtype: {card["cardtype"]}")
                self.cardtype.pack()
        if "supertype" in card and not card["supertype"] == []:
            if is_recursive:
                self.supertype0 = tk.Label(self, text=f"Supertype: {card["supertype"]}")
                self.supertype0.pack()
            else:           
                self.supertype = tk.Label(self, text=f"Supertype: {card["supertype"]}")
                self.supertype.pack()
        if "subtype" in card and not card["subtype"] == []:
            if is_recursive:
                self.subtype0 = tk.Label(self, text=f"Subtype: {card["subtype"]}")
                self.subtype0.pack()
            else:
                self.subtype = tk.Label(self, text=f"Subtype: {card["subtype"]}")
                self.subtype.pack()
        if "textbox" in card and not card["textbox"] == []:
            if is_recursive:
                self.textbox0 = tk.Label(self, text=f"{card["textbox"]}", wraplength=400)
                self.textbox0.pack()
            else:
                self.textbox = tk.Label(self, text=f"{card["textbox"]}", wraplength=400)
                self.textbox.pack() 
        if "keywords" in card and not card["keywords"] == []:
            if is_recursive:
                self.keywords0 = tk.Label(self, text=f"Keywords: {card["keywords"]}")
                self.keywords0.pack()
            else:
                self.keywords = tk.Label(self, text=f"Keywords: {card["keywords"]}")
                self.keywords.pack()
        if "quantity" in card and not card["quantity"] == []:
            if is_recursive:
                self.quantity0 = tk.Label(self, text=f"Quantity: {card["quantity"]}")
                self.quantity0.pack()
            else:
                self.quantity = tk.Label(self, text=f"Quantity: {card["quantity"]}")
                self.quantity.pack()
        if "number_in_deck" in card and not card["number_in_deck"] == []:
            if is_recursive:
                self.number_in_deck0 = tk.Label(self, text=f"Number in Decks: {card["number_in_deck"]}")
                self.number_in_deck0.pack()
            else:
                self.number_in_deck  = tk.Label(self, text=f"Number in Decks: {card["number_in_deck"]}")
                self.number_in_deck.pack()

        if is_recursive:
            self.build_card_page(item, False, is_dual_faced)
        else:
            self.add_button = tk.Checkbutton(self, text="Add", onvalue=1, offvalue=0)
            self.add_button.pack()


