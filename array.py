# // array creation , array func , file handling 
# // file read and write (r ,r+ , w,w+, etc  mode ) , change pointer positions and again write operation 
# // sink func at 10th position 
# Python list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Append
fruits.append("fig")
print("Fruit array after appending fig:", fruits)

# Insert "grape" at index 2
fruits.insert(2, "grape")
print("Fruit array after inserting grape at index 2:", fruits)

# Remove element at index 1
fruits.pop(1)
print("Fruit array after removing element at index 1:", fruits)

# Sort
fruits.sort()
print("Fruit array after sorting:", fruits)

# Reverse
fruits.reverse()
print("Fruit array after reversing:", fruits)

# Change first element
fruits[0] = "apricot"
print("Fruit array after changing first element to apricot:", fruits)

# # Iterating
# print("Iterating through the fruit array:")
# for fruit in fruits:
#     print(fruit)

# Length
print("Count:", len(fruits))

# Check empty
print("Is empty:", len(fruits) == 0)

# First and last
print("First element:", fruits[0] if fruits else None)
print("Last element:", fruits[-1] if fruits else None)

# Contains
print("Contains banana:", "banana" in fruits)

# Index of cherry
print("Index of cherry:", fruits.index("cherry") if "cherry" in fruits else None)
