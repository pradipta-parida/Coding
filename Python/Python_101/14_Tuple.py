"""

Tuple data type in python:

1. Tuple is immutable. i.e; once you have initialized, you can not modify again
2. So, we cant append, insert, delete etc... in tuple

"""

# To declare Tuple, we use ()
marks = (85, 45, 67)

# Basic operations in tuple
marks = (85, 45, 67, 67, 67)
print(marks.count(67)) # Output: 3

# To print index of any number
# In tuple, index starts from 0, 1, 2,...
print(marks.index(67)) # Output: 2

# If we don't assign any braces such as [], (), {} then by default python interprets as tuple
Student = "Reju", "Manji", "Sakuto"
print(Student) # Output: ('Reju', 'Manji', 'Sakuto') which is a tuple
