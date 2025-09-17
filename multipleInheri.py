# Parent class 1
class Electric:
    def battery(self):
        print("This car has a battery.")

# Parent class 2
class MusicSystem:
    def play_music(self):
        print("Playing music...")

# Child class (inherits from both)
class ElectricCar(Electric, MusicSystem):
    def drive(self):
        print("The electric car is driving.")

# Example usage
car = ElectricCar()
car.battery()      # from Electric
car.play_music()   # from MusicSystem
car.drive()        # from ElectricCar
