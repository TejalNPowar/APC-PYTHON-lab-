class stud:
    def __init__(self, name, age, grade):
      
        #Initialize the Car with specific attributes.
        self.name = name
        self.age = age
        self.grade = grade

# Creating an instance using the parameterized constructor
s = stud("Tejal",20,"A")
print(s.name)
print(s.age)
print(s.grade)