class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"{self.name} is moving in a generic way")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on water")

class Airplane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the air")

generic = Vehicle("Generic Vehicle")
car = Car("Toyota Camry")
boat = Boat("Sunset Cruiser")
plane = Airplane("Boeing 747")

generic.move()  
car.move()      
boat.move()     
plane.move()    