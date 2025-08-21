import array as arr
arr = arr.array('i',[1,2,3,4,5,6])  # arr.array(typecode,elements)
s = len(arr)
i = 0
print("Original array")
while s > 0:
    print(arr[i],end=" ")
    i = i +1
    s = s-1

s = len(arr)
# Append()
arr.append(3)
arr.append(7)
arr.append(7)

print("")
print("Append array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# insert()
arr.insert(1,6)
s = len(arr)
print("")
print("insert array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# pop
arr.pop()
arr.pop()
s = len(arr)
print("")
print("pop array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# remove
arr.remove(3)
s = len(arr)
print("")
print("remove array")
for i in range (len(arr)):
    print (arr[i], end=" ")

# index()
print("")
i = arr.index(5)
s = len(arr)
print(i)

# reverse()
arr.reverse()
s = len(arr)
print("reverse array")
for i in range (len(arr)):
    print (arr[i], end=" ")


# count()
s = len(arr)
print("")
print("count of 7 in array:", arr.count(7))

# is_empty()
if len(arr) == 0:
    print("Array is empty")
else:
    print("Array is not empty")


#first and last element 
if len(arr) > 0:
    print("First element:", arr[0])
    print("Last element:", arr[-1])

#is present
