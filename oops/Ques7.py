# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.


class Shopping_Cart:
    
    def __init__(self):
        self.items = []
    
    def add_items(self, item_name, quantity):
        item = (item_name, quantity)
        self.items.append(item)
    
    def remove_items(self, item_name):
        for item in self.items:
            if item[0] == item_name and item[1] > 0:
                self.items.remove(item)
                break
    
    def total_calculate(self):
        total = 0
        for item in self.items:
            total += item[1]

        return total

    
            