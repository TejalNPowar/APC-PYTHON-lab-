class student:
    def __init__(self,name,age ,grade):
        self.name=name
        print(f"Constructor called: Object is created for {self.name}")
    
        self.age=age
        print(f"Constructor called: Object is created for {self.age}")

        self.grade=grade
        print(f"Constructor called: object is created for {self.grade}")


    def display(self):
        print("Name:",self.name)  #public
        print("Age:",self._age)   #protected
        print("Grade:",self.__grade)   #private

s1=student("Tejal",23,"A")

print("Public:",s1.name)
print("Protected:",s1._age)
print("Private:",s1.__grade)

s1.display()


















# class Student:
#     def _init_(self, name, age, grade):
#         # Public member
#         self.name = name

#         # Protected member (convention: single underscore)
#         self._age = age

#         # Private member (name mangling: double underscore)
#         self.__grade = grade

#     def display(self):
#         print("Name:", self.name)          # public
#         print("Age:", self._age)           # protected
#         print("Grade:", self.__grade)      # private


# # Creating object
# s1 = Student("Rajnandini", 21, "A")

# # Accessing public member
# print("Public:", s1.name)

# # Accessing protected member (possible, but not recommended)
# print("Protected:", s1._age)

# # Accessing private member directly → ❌ Error
# # print(s1.__grade)   # AttributeError

# # Accessing private member using name mangling ✅
# print("Private:", s1.Student_grade)

# # Display using method
# s1.display()