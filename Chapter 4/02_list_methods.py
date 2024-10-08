l1 = [2,3,6,1,43,13,16,18]
print(l1)

# Sorts the list in ascending order (by default) or based on a key.
l1.sort()
print("\nSort: ",l1)

#  Reverses the order of the list in place.
l1.reverse()
print("Reverse: ",l1)

# Returns the number of occurrences of a specified element in the list.
count = l1.count(2)
print("Count of 2: ", count)

# Returns the index of the first occurrence of a specified element.
print("Index: ", l1.index(3))

# Adds an item to the end of the list.
l1.append(333)
print("Append: ", l1)

#  Inserts an element at a specified position.
l1.insert(8, 666)
print("Insert before 333: ",l1)

# Removes and returns the element at the given position (default is the last item).
l1.pop()  # default delete last element
print("Only pop: ", l1 )
l1.pop(0) # delete specified index element
print("Specified pop: ", l1)

# Removes the first occurrence of an element from the list.
l1.remove(16)
print("Remove: ", l1)

#  Extends the list by appending elements from another iterable (list, tuple, etc.).
l1.extend([55,66,77,88])
print("Extend: ",l1)

# Removes all items from the list.
l1.clear()
print(l1)