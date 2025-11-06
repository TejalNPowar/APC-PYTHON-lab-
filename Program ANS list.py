#1. Check if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# 2️⃣ Find the factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
    

# 3️⃣ Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))


# 4️⃣ Read contents from a file
file_name = input("Enter file name: ")
with open(file_name, 'r') as f:
    content = f.read()
    print("File Contents:\n", content)


# 5️⃣ Read from one file and write to another
with open('source.txt', 'r') as src:
    data = src.read()

with open('destination.txt', 'w') as dest:
    dest.write(data)

print("File copied successfully!")  


# 6️⃣ Display files in the current directory
import os
files = os.listdir('.')
print("Files in current directory:")
for f in files:
    print(f)



# 7️⃣ Horizontal bar chart of programming language popularity
import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(languages, popularity)
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')
plt.show()    


# 8️⃣ Create a pie chart
import matplotlib.pyplot as plt

labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [45, 30, 15, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Programming Language Popularity')
plt.show()


# 9️⃣ GUI using Tkinter
from tkinter import *

root = Tk()
root.title("Simple GUI")
root.geometry("300x200")

label = Label(root, text="Welcome to Tkinter!", font=('Arial', 14))
label.pack(pady=20)

btn = Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
btn.pack()

root.mainloop()



# 🔟 Class, Object, and Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Tejal", 20)
s1.display()


# 11️⃣ Method Overloading (Using default arguments)
class MathOperation:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Sum:", a + b + c)
        elif a is not None and b is not None:
            print("Sum:", a + b)
        else:
            print("Invalid arguments!")

obj = MathOperation()
obj.add(5, 10)
obj.add(2, 3, 4)


# 12️⃣ Method Overriding
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class")

obj = Child()
obj.show()



# 13️⃣ Single Inheritance
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()


# 14️⃣ Multilevel Inheritance
class Grandparent:
    def grand(self):
        print("This is Grandparent")

class Parent(Grandparent):
    def parent(self):
        print("This is Parent")

class Child(Parent):
    def child(self):
        print("This is Child")

c = Child()
c.grand()
c.parent()
c.child()




# 15️⃣ Array functions
import array

arr = array.array('i', [1, 2, 3, 4, 5])
arr.append(6)
arr.insert(2, 10)
arr.remove(4)
arr.reverse()
print("Array elements:", arr)
print("Index of 10:", arr.index(10))



# 16️⃣ List functions
lst = [10, 20, 30, 40]
lst.append(50)
lst.insert(2, 25)
lst.remove(20)
lst.reverse()
print("List:", lst)
print("Length:", len(lst))



# 17️⃣ Dictionary functions
d = {'name': 'Tejal', 'age': 20, 'city': 'Kolhapur'}
print(d.keys())
print(d.values())
d['college'] = 'DY Patil'
print(d.items())
d.pop('age')
print("After deletion:", d)



# 18️⃣ String functions
s = " Hello Python "
print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("Python", "World"))
print(s.split())



# 19️⃣ Tuple functions
t = (1, 2, 3, 2, 4)
print("Count of 2:", t.count(2))
print("Index of 3:", t.index(3))
print("Length:", len(t))
print("Max:", max(t))
print("Min:", min(t))



# 20️⃣ Set functions
s = {1, 2, 3, 4, 5}
s.add(6)
s.remove(3)
print("Union:", s.union({7, 8}))
print("Intersection:", s.intersection({4, 5, 6}))
print("Set elements:", s)



# 21️⃣ Function and Lambda Function
def square(x):
    return x * x

lambda_square = lambda x: x * x

print("Function result:", square(5))
print("Lambda result:", lambda_square(5))



# 22️⃣ Package for addition & multiplication

# File: mypackage/calc.py

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b


# Main program:

# from mypackage import calc

# x, y = 5, 3
# print("Addition:", calc.add(x, y))
# print("Multiplication:", calc.multiply(x, y))



# 23️⃣ Stemming using NLTK
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
words = ["running", "flies", "easily", "fairly"]
for w in words:
    print(w, "->", ps.stem(w))



# 24️⃣ Use of NumPy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Square Root:", np.sqrt(arr))
print("Reshaped Array:\n", arr.reshape(5, 1))



# 25️⃣ Use of Pandas
import pandas as pd

data = {'Name': ['Tejal', 'Riya', 'Aarav'], 'Age': [20, 21, 19]}
df = pd.DataFrame(data)
print(df)
print("Describe:\n", df.describe())
print("Head:\n", df.head())
print("Select column:\n", df['Name'])
print("Shape:", df.shape)