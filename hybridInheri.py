# Parent class
class Animal:
    def eat(self):
        print("Animals can eat.")

# Child class 1 (inherits Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof!")

# Child class 2 (inherits Animal)
class Cat(Animal):
    def meow(self):
        print("Cat meows: Meow!")

# Grandchild class (inherits both Dog and Cat → Hybrid)
class Puppy(Dog, Cat):
    def weep(self):
        print("Puppy weeps: Yip! Yip!")

# Example usage
p = Puppy()
p.eat()    # from Animal
p.bark()   # from Dog
p.meow()   # from Cat
p.weep()   # from Puppy
