# Parent class
class Person:
    def greet(self):
        print("Hello! I am a person.")

# Child class 1
class Student(Person):
    def study(self):
        print("I am studying.")

# Child class 2
class Teacher(Person):
    def teach(self):
        print("I am teaching.")

# Example usage
s = Student()
t = Teacher()

s.greet()   # from Person
s.study()   # from Student

t.greet()   # from Person
t.teach()   # from Teacher
