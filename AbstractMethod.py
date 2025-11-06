from abc import ABC, abstractmethod

class Animal(ABC):             # Abstract class
    @abstractmethod
    def sound(self):           # Abstract method
        pass                   # No implementation

class Dog(Animal):             # Subclass
    def sound(self):           # Must implement sound()
        print("Bark 🐶")

# obj = Animal() ❌ Error: Can't instantiate abstract class
d = Dog()
d.sound()
