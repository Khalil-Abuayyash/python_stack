from product import Product

class Store:

    def __init__(self,name,list=[]):
        self.name = name
        self.list = list

    def  add_product(self, new_product):
        self.list.append(new_product)
        return self

    def sell_product(self, id):
        self.list[id].print_info()
        list.pop(id)
        return self

    def inflation(self, percent_increase):
        for item in self.list:
            item.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for item in self.list:
            if item.category == category:
                item.update_price(percent_discount, False)
        return self
    
    def print_all_products_info(self):
        for item in self.list:
            item.print_info()

# Real = Store("Real")
# Real.add_product(Product("yellow_apple", 2, "Fruits")).add_product(Product("Grapes", 5, "Fruits")).add_product(Product("Tomato", 3, "Vegetables"))
# Real.list[0].update_price(0.05, True).print_info()
# Real.inflation(0.5).print_all_products_info()
# Real.set_clearance("Fruits", 0.5).print_all_products_info()
    
