mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

x[1]= 'orange'  # error because frozensets are immutable

