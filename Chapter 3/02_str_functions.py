str = "  this tutorial is ,very intresting"

# Returns length
print("Lenght: ",len(str))

# Returns lower case
print("Lower case: ", str.lower())

# Returns upper case
print("Upper case:", str.upper())

# Removed white space and character from start and end of string
print("Striped:",str.strip()) 

# Replaces occurrences of a substring with another substring.
print("Replaced String: ", str.replace("intresting", "helpfull"))

# Splits the string into a list of substrings based on the given separator.
print("Split: ", str.split(","))

# Returns the index of the first occurrence of a substring. Returns -1 if not found.
print("Find: ", str.find("g"))

# Returns the number of occurrences of a substring in the string.
print("Count: ", str.count("i"))

# Checks if the string starts with the specified substring. Returns True or False.
print("Starts with: ", str.startswith("  this"))

# Checks if the string ends with the specified substring. Returns True or False.
print("Ends with: ", str.endswith("xyz"))

# Checks if all characters in the string are alphabetic (no digits or special characters). Returns True or False.
print("Is alpha: ", str.isalpha())

#  Checks if all characters in the string are digits. Returns True or False.
print("Is digit: ", str.isdigit())

# Converts the first letter of each word in the string to uppercase and the rest of the letters to lowercase.
print("Titled: ", str.title())

str2 = "this tutorial is ,very intresting"
# Converts the first letter of the entire string to uppercase and makes all the other characters lowercase.
print("Capitalize: ", str2.capitalize())
