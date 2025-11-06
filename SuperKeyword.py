class Animal:
    def sound(self):
        print("animal make a sound ")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dogs can Bark")

d=Dog()
d.sound()