# from abc import ABC, abstractmethod

# class Animal(ABC):   # inherits from ABC → abstract class
#     @abstractmethod
#     def sound(self):   # abstract method
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Bark 🐶")

# class Cat(Animal):
#     def sound(self):
#         print("Meow 🐱")

# # obj = Animal()  ❌ Error: Can't instantiate abstract class
# d = Dog()
# c = Cat()

# d.sound()
# c.sound()


from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        print("Bark")
class cat(Animal):
    def sound(self):
        print("Meow")

# obj = Animal()
d=dog()
c=cat()

d.sound()
c.sound()