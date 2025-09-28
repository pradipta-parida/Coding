"""
String Modifications:

We can modify a given string to uppercase, lowercase etc...

For convenience, use '' for characters

and "" for strings

"""
from traceback import print_tb

name = "Tony Stark"

print(name.upper())

print(name.lower())

print(name.capitalize())

# position start from 0,1,2...
# In case the character is not present it will give output as -1
# We can use to find word as well
print(name.find('S'))
print(name.find('s'))
print(name.find('z'))
print(name.find("tark"))

# To replace entire string and this does not store the value of new string
print(name.replace("Tony Stark","Iron Man"))
print(name)

# To replace a part of string. i.e; sub-string
print(name.replace("To", "Chako"))

# We can replace characters as well. If the replace character is not there, then it will ignore.
print(name.replace("y", "i"))
print(name.replace("Y", "i"))
