import tkinter as tk

class card_page(tk.Frame):
    def __init__(self, item, p_frame):
            super().__init__(p_frame)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.name = tk.Label(self, text=f"{item["name"]}")
            self.name.grid(row=0,column=0) 
            if "cost" in item and not item["cost"] == [] and not item["cost"]=="":
                self.cost = tk.Label(self, text=f"cost: {item["cost"]}")
                self.cost.grid(row=0,column=1)             
            if "cmc" in item and not item["cmc"] == []:
                self.cmc = tk.Label(self, text=f"cmc: {item["cmc"]}")
                self.cmc.grid(row=0,column=2) 
            if "color_id" in item and not item["color_id"] == []:
                self.color_id = tk.Label(self, text=f"color_id: {item["color_id"]}")
                self.color_id.grid(row=0,column=3) 
            if "cardtype" in item and not item["cardtype"] == []:
                self.cardtype = tk.Label(self, text=f"cardtype: {item["cardtype"]}")
                self.cardtype.grid(row=1,column=0) 
            if "supertype" in item and not item["supertype"] == []:
                self.supertype = tk.Label(self, text=f"supertype: {item["supertype"]}")
                self.supertype.grid(row=1,column=1) 
            if "subtype" in item and not item["subtype"] == []:
                self.subtype = tk.Label(self, text=f"subtype: {item["subtype"]}")
                self.subtype.grid(row=1,column=2) 
            if "textbox" in item and not item["textbox"] == []:
                self.textbox = tk.Label(self, text=f"{item["textbox"]}", wraplength=400)
                self.textbox.grid(row=2,column=0, columnspan=3) 
            if "keywords" in item and not item["keywords"] == []:
                self.keywords = tk.Label(self, text=f"keywords: {item["keywords"]}")
                self.keywords.grid(row=3,column=0) 
            if "quantity" in item and not item["quantity"] == []:
                self.quantity = tk.Label(self, text=f"quantity: {item["quantity"]}")
                self.quantity.grid(row=3,column=1) 
            if "number_in_deck" in item and not item["number_in_deck"] == []:
                self.number_in_deck  = tk.Label(self, text=f"number in decks: {item["number_in_deck"]}")
                self.number_in_deck.grid(row=3,column=2)         
            if "card_faces" in item and not item["card_faces"] == []:
                self.card_faces = tk.Label(self, text=f"is dual faced")
                self.card_faces.grid(row=3,column=3) 
