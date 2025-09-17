
# import sys
# print(sys.path)  # shows Python’s search paths

from MyPackage.student import Student

# Creating objects
s1 = Student("Tejal", 101)
s2 = Student("Riya", 102)

print("Objects are in use...")

# Delete one object manually
del s1

print("End of program")
