""" Loop (Infinite Loop), to keep on dice rolling until and unless the user inputs no
    # Ask: roll the dice?
    # If user enters y
    #   Generate two random numbers
    #   Print them
    # If user enters n
    #   Print thank you message
    #   Terminate
    # Else
    #   Print invalid choice
"""

"""
A formatted string, or f-string, in Python is a type of string literal that makes it easy to embed variables,
expressions, and even function calls directly into strings by enclosing them in curly braces {} and prefixing the string with f. F-strings were introduced in Python 3.6 and are now considered the modern, efficient way to perform string formatting.

Syntax and Basic Example
To use an f-string, prefix the string with the letter f and include any variable or expression inside curly braces.

Example:

python
name = "Alice"
age = 30
print(f"Hello, {name}. You are {age} years old.")
This will display: Hello, Alice. You are 30 years old.
"""



# Import Module for random number generation
import random

# The statement while True: in Python starts an infinite loop, meaning the code inside the loop will execute repeatedly until it is stopped by a break statement or another exit condition.
# The colon (:) is required at the end to indicate the start of the loop’s code block, and the body of the loop must be properly indented.
while True:
    user_choice = str(input("Roll the dice? (Y/N): ")).lower()  # We have put this such as to loop it again for user to prompt for input
    if user_choice == "y":
        die1 = random.randint(1, 6)    #This randint function will generate random number between 1 to 6
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')           # {} is used for placeholders or a hole in our string

    elif user_choice == "n":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice!")
