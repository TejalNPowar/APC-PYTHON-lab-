class OneDArray:
    def __init__(self, elements):
        self.elements = elements  # store array elements

    def display(self):
        print("1D Array Elements:", self.elements)

# create object
arr1 = OneDArray([10, 20, 30, 40, 50])
arr1.display()


class TwoDArray:
    def __init__(self, matrix):
        self.matrix = matrix  # list of lists

    def display(self):
        print("2D Array (Matrix):")
        for row in self.matrix:
            print(row)

# create object
arr2 = TwoDArray([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
arr2.display()


import numpy as np

class ThreeDArray:
    def __init__(self, elements):
        self.arr = np.array(elements)

    def display(self):
        print("3D Array:\n", self.arr)

# Object
obj3 = ThreeDArray([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
obj3.display()
