class FoodOrder :
    def __init__(self, customer_name, item, price):
        self.customer_name = customer_name
        self.item = item
        self.price = price

order1 = FoodOrder("anuja", "pizza", 100)
order2 = FoodOrder("Anuja ", "pizza", 200)
print(order1.customer_name, order1.item, order1.price)
print(order1.customer_name, order2.price)
order1.show_order()

'''
inside class : only define methods and attributes
outside class :call
'''