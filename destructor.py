class Student:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called: Object created for {self.name}")

    def __del__(self):
        print(f"Destructor called: Object destroyed for {self.name}")
        
# object creation
s1 = Student("Tejal")

# object deletion
del s1

print("Program finished")
