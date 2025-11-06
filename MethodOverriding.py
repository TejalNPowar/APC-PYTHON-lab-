class Parent:
    def show(self):
        print("This is the Parent class method")

class Child(Parent):
    def show(self):
        print("This is the Child class method")

obj = Child()
obj.show()
3