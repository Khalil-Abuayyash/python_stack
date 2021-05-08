class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price + percent_change * self.price
        else:
            self.price = self.price - percent_change * self.price
        return self

    def print_info(self):
        print(f"product-Name: {self.name}, product_Price: {self.price}, product_Category: {self.category}")
        return self