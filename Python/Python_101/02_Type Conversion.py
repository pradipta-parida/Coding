"""
Type-conversions:
We can only con-catenate type of similar data type.
So, to do operations with string and int we need to convert the int to string ad then only con-catenate will happen

"""

# This would throw type exception
'''
old_age = input("What is your old age?")

new_age = old_age + 3

print(new_age)

'''

# To overcome this we need to convert it to appropriate type

old_age = input("What is your old age?" + " ")

old_age = int(old_age)

new_age = old_age + 3

print(new_age)

# More Examples of Type Conversions;
number = 18
print(float(number))
