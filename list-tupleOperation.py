my_list=[1,2,3,4,5]
print("First list element:", my_list[0])
print("Last list element:", my_list[-1])

my_list.append(6)
print("List after appending 6:", my_list)

my_list.remove(3)
print("List after removing 3:", my_list)

my_list.pop(1)
print("List after popping element at index 1:", my_list)

my_list.insert(2, 10)  
print("List after inserting 10 at index 2:", my_list)

my_list.index(4)
print("Index of element 4 in list:", my_list.index(4))

my_list.count(2)
print("Count of element 2 in list:", my_list.count(2))

my_list.sort()
print("List after sorting:", my_list)

my_list.reverse()
print("List after reversing:", my_list)



#TUPLE OPERATIONS
my_tuple = (1, 2, 3, 4, 5)
print("First tuple element:", my_tuple[0])
print("Last tuple element:", my_tuple[-1])
print("Tuple length:", len(my_tuple))
print("Index of element 3 in tuple:", my_tuple.index(3))
print("Count of element 2 in tuple:", my_tuple.count(2))
print("Tuple as a list:", list(my_tuple))
my_tuple2 = (6, 7, 8)
combined_tuple = my_tuple + my_tuple2
print("Combined tuple:", combined_tuple)
print("Tuple after slicing (1:4):", my_tuple[1:4])
print("Tuple after slicing (2:):", my_tuple[2:])
print("Tuple after slicing (:):", my_tuple[:])
print("Tuple after slicing (:-1):", my_tuple[:-1])
print("Tuple after slicing (1:3):", my_tuple[1:3])




#SET OPERATIONS
my_set = {1, 2, 3, 4, 5}
print("Set elements:", my_set)
print("Set length:", len(my_set))
print("Is 3 in set?", 3 in my_set)
my_set.add(6)
print("Set after adding 6:", my_set)
my_set.remove(2)
print("Set after removing 2:", my_set)
my_set.discard(10)  
print("Set after discarding 10 (not present):", my_set)
my_set.clear()
print("Set after clearing:", my_set)
my_set = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
print("Set union:", my_set.union(my_set2))


my_set = set([1, 2, 3, 4, 5])#set using set function
print("Set created using set function:", my_set)
