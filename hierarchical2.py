# Parent class
class Vehicle:
    def show(self):
        print("This is a vehicle.")

# Child class 1
class Bike(Vehicle):
    def type(self):
        print("This is a Bike.")

# Child class 2
class Car(Vehicle):
    def type(self):
        print("This is a Car.")

# Child class 3
class Bus(Vehicle):
    def type(self):
        print("This is a Bus.")

# Child class 4
class Truck(Vehicle):
    def type(self):
        print("This is a Truck.")


# Example usage
b1 = Bike()
c1 = Car()
bus1 = Bus()
t1 = Truck()

b1.show()
b1.type()

c1.show()
c1.type()

bus1.show()
bus1.type()

t1.show()
t1.type()
