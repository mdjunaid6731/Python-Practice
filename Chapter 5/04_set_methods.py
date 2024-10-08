s = {1,4,5,4,3,2,66}

# Adds an element to the set. If the element is already present, it does nothing.
s.add(555)
print(s)

#len of set
print(len(s))

# Removes the specified element from the set. Raises a KeyError if the element is not found.
s.remove(5)
print(s)

# Removes the specified element from the set if it exists. Does not raise an error if the element is not found.
s.discard(99)
print(s)  #no error

# Returns a new set that is the union of the set and the specified sets.
s2 = {1,2,9,8,0}
union_set = s.union(s2)
print(union_set)

# Returns a new set with elements that are common to the set and all the specified sets.
intersect = s.intersection(s2)
print(intersect)
 
#  Returns a new set with elements that are in the set but not in the other specified sets.
diff_set = s.difference(s2)
print(diff_set)

# Returns a new set with elements that are in either set but not in both.
sym_set = s.symmetric_difference(s2)
print(sym_set)

# Returns True if all elements of the set are in the other set.?
print(s.issubset(s2))

# Returns True if the set contains all elements of the other set.
print(s.issuperset(s2))

# Removes all elements from the set, making it empty.
s.clear()
print(s)