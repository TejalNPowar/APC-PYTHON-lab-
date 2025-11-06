import numpy as np
#_______________________________ 1D _____________
n = int(input("Enter number of elements for 1D array: "))
one_d = np.array([int(input(f"Enter element {i+1}: ")) for i in range(n)])

print("\n1D Array:")
print(one_d)
# _________________________2D_______________________________________________

x = int(input("Enter number of 2D matrices: "))
rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

three_d = np.array([
    [[int(input(f"Enter element [{i+1}] [{j+1}][{k+1}]: ")) for k in range(cols)]
    for j in range(rows)] for i in range(x)
])

print("\n3D Array:")
print(three_d)

# ____________3D____________

x = int(input("Enter number of 2D matrices: "))
rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

three_d = np.array([
    [[int(input(f"Enter element [{i+1}] [{j+1}][{k+1}]: ")) for k in range(cols)]
    for j in range(rows)] for i in range(x)
])

print("\n3D Array:")
print(three_d)

