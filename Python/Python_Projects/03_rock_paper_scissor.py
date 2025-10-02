"""
1. Ask the user to make a choice
2. If choice is not valid
3.      Print the error
4. If choice is valid
5  Let the computer make a choice
6  Print the choices
7. Determine the winner
8. Ask the user if they want to continue
9. If not
10. Terminate the program
"""

import random

# Define emojis for better UI experience. This is a dictionary of key-value pairs
emojis = {"r":"🪨", "p":"📃", "s":"✂️" }

# Since list can be modified by accidentally removing it. So, we are going to use tuple which is immutable(cant be removed or append).
# choices = ['r', 'p', 's']
choices = ('r', 'p', 's')
"""
# Refactoring our code

We can define getting user choice in a function.

def get_user_choice():
    while True:
        user_choice = str(input("Rock, Paper, Scissors? (r/p/s): ")).lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")
        
def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    
def determine_winner(user_choice, computer_choice):
     if user_choice == computer_choice:
        print("Draw!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("You win!")

    else:
        print("You lose!")

def play_game():        
    while True:
        user_choice = get_user_choice()
        
        computer_choice = random_choice(choices)
        
        display_choices(user_choice, computer_choice)
        
        determine_winner(user_choice, computer_choice)
        
        if should_continue == "n":
            print()
            print("Thank you for playing!")
            break

# To call our function while running our code            
play_game()
"""


# The statement while True: in Python starts an infinite loop, meaning the code inside the loop will execute repeatedly until it is stopped by a break statement or another exit condition.
# The colon (:) is required at the end to indicate the start of the loop’s code block, and the body of the loop must be properly indented.
while True:
    # User would provide input and the input will be converted to lower case
    user_choice = str(input("Rock, Paper, Scissors? (r/p/s): ")).lower()

    # continue statement here will validate if the user input is invalid then go back to above user_choice.
    # How continue Works?
    # continue keyword can only be used in loops.
    # When Python encounters continue inside a loop, it skips all the remaining code in that iteration.
    # It then goes back to the start of the loop to check the condition and continue with the next iteration if the condition is true.
    if user_choice not in choices:
        print("Invalid choice")
        continue

    # In random module functions, we have choice() which takes list or tuple data types.
    # Here, it would pick random value from r, p, s from the choices tuple
    computer_choice = random.choice(choices)

    # For coders to know what the computer has choice
    # Here, we use formatted string. So, we prefix the string with f which is short for formatted and here we add curly braces
    # to insert a value dynamically, for example user_choice / computer_choice.
    # With help of this we don't have to use concatenation
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Draw!")

    # Here we use logical (or) operator to combine two set of conditions
    # Another approach is using parenthesis for multi-line without any \
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("You win!")

    else:
        print("You lose!")

    # Asking user if they want to continue or not
    should_continue = input("Continue? (y/n): ").lower()

    if should_continue == "n":
        print()
        print("Thank you for playing!")
        break
