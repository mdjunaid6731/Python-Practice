# What will be the length of following set

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))  #returns 2 

# In python 20 == 20.0 is True, camparision operator check values 