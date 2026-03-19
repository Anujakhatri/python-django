# suppose you are working for daraz application and u have to work for new brand of laptop
# create a class Laptop with brand, price and method show_details() ,

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price= price
    def show_detail(self):
        print("Brand Name : {}".format(self.brand))
        print("Price: {} ".format(self.price))
laptop1 = Laptop ("Asus", 80000)
laptop2 = Laptop("Dell", 90000)
print(laptop1)
print(laptop2)
laptop1.show_detail()
laptop2.show_detail()
