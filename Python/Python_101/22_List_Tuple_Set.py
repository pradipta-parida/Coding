"""
List[], Tuple() and Set{}:

1. How do we get to know where to use List, Tuple and Set
2. Below are the differences b/w them

"""


""" Syntax difference """

''' List '''
# List keeps duplicates
# Lists are ordered. In an ordered collection each item has position, also called as index 0, 1, 2, 3..
# Assigning the list to a variable, we can use indexes to access any of the items.
# List can be modified after creation (a trait called mutable). Hence, Lists are mutable.
my_list = ['a', 'b', 'c', 'a']
print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[2])
my_list.append('d') # Adding
my_list.remove('b') # Removing
my_list[1] = 'x' # Reassigning
print(my_list)

''' Tuple '''
# Tuple keeps duplicates
# Tuples are ordered
# Assigning the tuple to a variable, we can use indexes to access any of the items.
# Tuple can't be modified after creation (a trait called immutable). Hence, Tuple are immutable.
# In situations where keeping your data safe from accidental changes is more important than flexibility
my_tuple = ('a', 'b', 'c', 'a')
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[2])
# my_tuple.append('d') # No Append or remove methods
# my_tuple.append('d')
# [1] = 'z' #TypeError: 'tuple' object does not support item assignment. Since, its immutable.

''' Set '''
# Set automatically drop duplicates - useful when we want to eliminate duplicate values from collection
# Sets are unordered, which means its items are not assigned a position or index.
# If we assign our set to a variable and try to index it, we get an error
# Sets are like list, it's mutable.
# But since sets are unordered and don't have indexes, we can't directly update a specific item.
# Instead, to change an item in a set, for example the letter B to the letter D, we remove the unwanted B and append the new D.
#
my_set = {'a', 'b', 'c', 'a'}
print(my_set)
print(type(my_set))
print(len(my_set))
#print(my_set[2]) # O/P: TypeError: 'set' object is not subscriptable as set is unordered
my_set.add('x')
print(my_set)
my_set.remove('a')
print(my_set)
my_set.remove('b')
print(my_set)
my_set.add('d')
print(my_set)

# Example of set
'''
Lets suppose we have list of numbers and want to get only the unique values.
We can do this by simply converting the list into a set, which automatically filters out
the repeated values.
Then, if we want to work with a list again, we can simply cast the set back into a list 
'''
nums = [1, 3, 3, 1, 2, 4, 5, 2, 4]
set(nums)
print(set(nums))
# Cast the set back to list
list(set(nums))
print(list(set(nums)))

# Example of Tuple
'''
We want to store a friend's birthday in our program. Because a birthday is a piece of information 
that shouldn't change once its assigned. Storing this type of information in a tuple is a good idea.
It helps protect the data and prevents it from being accidentally modified later in the program.
'''


