# Parent class
class Animal:
    def eat(self):
        print("Animals can eat.")

# Child class (inherits Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")

# Grandchild class (inherits Dog)
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps: Yip! Yip!")

# Example usage
p = Puppy()
p.eat()    # from Animal
p.bark()   # from Dog
p.weep()   # from Puppy















