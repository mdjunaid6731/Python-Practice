d = {} #empty dict

print(type(d))
marks = {
    "Johan" : 100,
    "Shubham" : 70,
    "Rohan" : 78
}

print(marks.items()) #return list  of each item in tuple
print(marks.keys())  #return keys
print(marks.values()) #retun values in list
marks.update({"Johan":98, "Akash": 60})  # value updat add can also add new item
print(marks)

#Both give same output , what is differnce? 
print(marks.get("Johan"))   # returns none if key  does not exist
print(marks["Johan"])   #returns error if key  does not exsit

# Returns a shallow copy of the dictionary.
new_dict = marks.copy()
print(new_dict)

# Removes the specified key and returns the value. If the key is not found, returns the default value.
marks.pop("Akash")
print(marks)

# Removes and returns the last inserted key-value pair as a tuple.
print(marks.popitem())

# Removes all items from the dictionary.
marks.clear()
print(marks)