class Ride:
    class Ride:
        def __init__(self, user, distance):
            self.user = user
            self.__distance = distance #private used for encapsulation
        def get_distance(self):
            return self.__distance

        def set_distance(self, distance):
            if distance > 0 :
                self.__distance = distance
    r = Ride("Anuja", 5)
    print(r.set_distance(10))

        # def fare(self):
        #     print(self.distance)
        #     print("this is for calculation of fare ")

    class BikeRide(Ride):  # inheritance
        def __init__(self, user, distance):
            super().__init__(user, distance)

        def fare(self):
            print("this is bike fare ", self.distance * 50)

    class CarRide(Ride):
        def __init__(self, user, distance):
            super().__init__(user, distance)

        def fare(self):
            print("this is car fare ", self.distance)
            print(self.distance * 100)

    r1 = BikeRide("jagriti", 5)
    r1.fare()
    r2 = CarRide("bikita", 15)
    r2.fare()

    #Polymorphism
#Polymorphism means "many forms"
# The same method name behaves differently depending on the object calling it.

   #Encapsulation
#Hiding the internal data of an object