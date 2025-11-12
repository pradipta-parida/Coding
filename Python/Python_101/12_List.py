"""

List in Python:

List is a collection of data types. (Primitive data types)

"""

# To initiate and store different data types in list
marks = [95, 88, 47, 70, 55, "maths"]
print(marks)

# To print a particular value in list
# [-1] index in python states that start counting from reverse
print(marks[0])
print(marks[2])
print(marks[-1])
print(marks[-2])
'''
print(marks[-7]) # [-7] index does not exist in above list
print(marks[6])  # [6] index does not exist in above list
'''

# To print a subset or part of list.
print(marks[1:4]) # This will include only index of 1, 2, 3 only not 4
# O/P: [88, 47, 70]

# List using Loop
marks = [95, 88, 47, 70, 55, "maths"]
for score in marks:
    print(score)

# To append or add new marks into our existing list
# This will add the value at last index of the list
marks.append(22)
print(marks)

# To insert a value to the list
# This will insert the value at the specified index of the list.
# To declare that, (index, value)
marks.insert(2, 39)
marks.insert(0, 69)
print(marks)

# To check and verify if a value exists in our list
print(95 in marks)
print(10 in marks)

# To print length of our list
print(len(marks)) # Length starts from 1, 2, 3, ....,9

# List using while loop
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

# To clear your list values
marks.clear()
print(marks)
