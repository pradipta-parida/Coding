"""

Range in Python:

It means navigating from one value to another value.

Note: Last number does not get included in this.

Range starts from 0 by default.

However, If we want to change this lower bound, we can specify it as first argument.
"""

numbers = range(5)
print(numbers)
# O/P:-  0, 1, 2, 3, 4

# To print numbers within given range
for item in range(5):
    print(item)

# To include print of end limit of range
print()
for item in range(5):
    print(item + 1)

# To specify lower boundary values in our range
print()
for item in range(1000, 1006):
    print(item)