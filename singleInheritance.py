# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Example usage
d = Dog()
d.sound()   # method from parent
d.bark()    # method from child
