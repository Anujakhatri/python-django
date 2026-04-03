class Restaurant:
    menu ={
        "momo": 140,
        "pizza": 350,
        "pasta": 200,
        "noodles": 150,
        "Ice Cream": 100
    }

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.order = []
        self.order_summary ={}
        self.discount = 0

    def place_order(self, item, quantity):
        if item in Restaurant.menu:
            price = Restaurant.menu[item] * quantity
            order = (item, quantity, price) #tuple
            self.order.append(order)
            print(f"{self.customer_name} ordered {quantity} x {item} successfully")
        else:
            print(f"Sorry, {item} is not available in menu")

    def apply_discount (self, percent):
        self.discount = percent
        print(f"A {percent}% discount has been applied for {self.customer_name}")

    def calculate_total(self):
        total_order = lambda order: order[2]  # Lambda function to get price
        total = sum(total_order(order) for order in self.order)  # Loop + sum
        if self.discount > 0:
            total = total - (total * self.discount / 100)  # Apply discount
        return total

    def unique_items_ordered(self):
        return set(item[0] for item in self.order)

    def show_summary(self):
        print("\n -----Order Summary for", self.customer_name, "------")
        print("Item-wise quantity :", self.order_summary)     #dictionary format
        print("Unique items ordered :", self.unique_items_ordered()) #set
        print("Total bill after discount:", self.calculate_total(), "INR")
        print("--------------------------------------\n")


customer1 = Restaurant("Anuja")
customer2 =Restaurant("Aakriti")
customer1.place_order("momo", 3)
customer1.apply_discount(10)
customer1.show_summary()