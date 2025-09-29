"""

While Loops in Python:

Till the condition is True, until then the while block of code gets executed.

"""

# initialize a variable
i = 1
while i <= 5:
    print(i)
    i += 1

# Print star pattern
# If we multiply string with any number then that string gets multiplied that many times
i = 1
while i <= 5:
    print(i * "*")
    i += 1

# Print star pattern (inverted)
i = 5
while i >= 0:
    print(i * "*")
    i -= 1
