# // constructor default aani parameterised 
# // destructor 
# // private single inverted inser krun 
# // protected // scopes 
# // package 

#default constructor

class Car:
    def __init__(self):

        #Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

# Creating an instance using the default constructor
car = Car()
print(car.make)
print(car.model)
print(car.year)