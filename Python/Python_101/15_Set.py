"""
Set in python:

1. To store collection of data types but it should be of unique value.
2. Set is also called as Un-ordered collection.
"""

# To declare a set, use {}
marks = {95, 98, 97, 97, 68}
print(marks) # Output: {97, 98, 68, 95} as it takes unique values only

# There is no index concept in sets.
#print(marks[0]) # Output: TypeError: 'set' object is not subscriptable

# To print set using for loop
for score in marks:
    print(score)
