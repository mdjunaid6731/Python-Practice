name = "Mohammed junaid"
# name = 'Mohammed junaid'
# name = '''Mohammed junaid'''

# String slicing 
print(name[0:3]) # returns moh
print(name[2:8]) # returns hammed
print(name[:15]) # returns mohammed junaid
print(name[0:]) # returns mohammed junaid


# Negative indexing
print(name[-4:-1])  # covert correspondence positive indexing 
print(name[11:14])  # returns nai same as print(name[-4:-1])

# skip value
print(name[1:5:2])  # returns oa  ,2 step forword
print(name[1:12:3])  # returns omdu , 3 step forword
print(name[::-1])  # returns dianuj demmahoM
