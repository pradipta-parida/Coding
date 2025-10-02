"""
1. Generate a random number between 1 and 100
2. Ask the user to make a guess
3. If not a valid number
    Print an error
4. If number < guess
    Print too low
5. If number > guess
    Print too high
"""

import random

random_number = random.randint(1, 100)  # Here, we have put it out of the while loop, because we want to generate random number only once.

# For coder, to know the random number
# print(random_number)

# Here, we need to user try-except block, if user enters invalid entry such as a, % likewise then this will handle ValueError, that appears on the console,
# The statement while True: in Python starts an infinite loop, meaning the code inside the loop will execute repeatedly until it is stopped by a break statement or another exit condition.
# The colon (:) is required at the end to indicate the start of the loop’s code block, and the body of the loop must be properly indented.
while True:
    try:
        user_number = int(input("Guess a number between 1 and 100: "))

        if user_number > random_number:
            print("Your number is too high")

        elif user_number < random_number:
            print("Your number is too low")

        else:
            print("Congratulations! You guessed the number")
            break

    except ValueError:
        print("Please enter a valid number.")
