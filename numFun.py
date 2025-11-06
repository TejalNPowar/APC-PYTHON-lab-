import numpy as np

# 1.reshape()
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)   # 2 rows, 3 columns
print("Original Array:", arr)
print("Reshaped Array:\n", reshaped)
# ______________________________________________________

# 2.flatten()
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
flat = arr2.flatten()
print("Flattened Array:", flat)
# __________________________________________________________

# 3.transpose
arr1 = np.array([[1, 2, 3],
                [4, 5, 6]])

trans = arr1.transpose()
print("Transposed Array:\n", trans)
# __________________________________________________________

# 4.arange()
arr4 = np.arange(1, 11, 2)   # start=1, stop=11, step=2
print("Array:", arr4)

# _______________________________________________________
# 5.linspace
arr5 = np.linspace(0, 1, 5)  # start=0, stop=1, total=5 points
print("Array:", arr5)

# __________________________________________________________
# 6.ones(),zeros(), eye()
print(np.ones((2, 3)))   # 2x3 matrix of 1s
print(np.zeros((3, 2)))  # 3x2 matrix of 0s
print(np.eye(3))         # 3x3 identity matrix

# _______________________________________________________
# 7.sum(),mean(),max(),min()
arr = np.array([10, 20, 30, 40])
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())

# _________________________________________________________
# 9.concatenate()
a=np.array([1,2,3])
b=np.array([4,5,6])
join= np.concatenate((a,b))
print("Concatenated Array:",join)

# _________________________________________________________
#10. reshape()  vs resize()
ar=np.array([1,2,3,4,5,6])
new_ar=ar.reshape(2,3)
print("Reshaped (original unchanged:)\n",new_ar)

ar.resize(2,3)
print("Resize (original changed):\n",ar)


