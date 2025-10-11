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

# Another example of while loop
count =1

while count <= 5:
    # code to Repeat
    print("count =", count)
    count += 1
# Code not part of loop body
print("End of the program")
print()

# Example of for loop
for count in range(1, 6):
    print(f"Count = {count}")
    count =+ 1
# Code not part of loop body
print("End of the program")

""" Usage of while and for loops in Python:"""

'''
For loop is used where we know the number of iterations before the loop starts running.
However, the limitations of for loop is that we must know the number of iterations in advance to use them.

While loop is used where we dont know the number of iterations before the loop starts running.
For example, password entering where we dont know user attempts to provide valid creds
'''

# Another example of while loop
user_input = ""
while user_input != "secret123":
    user_input = input("Enter your password: ")
print("Access Granted")

