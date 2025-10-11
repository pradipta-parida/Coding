
"""
Error Handling: Handle errors/ exceptions!
Value error is one of the common errors.

To fix this or Tell the user:
1. What went wrong
2. How to fix the issue

This is where try and except keywords come in.
We'll use above keywords to help us manage unexpected exceptions.

Under the try statement, we indent => code that could cause an exception
If an exception occurs, during the execution of the try block, Python stops executing the try block
and moves down to the except block.

In the except block, we write code that either addresses the exception or outputs an instruction for the user.

If the execution of the try block does not generate an exception, the except block is skipped.

"""

''' Sample Program '''
# User input on Numerator and Denominator
#numerator = float(input("Enter your numerator: "))
#denominator = float(input("Enter your denominator: "))

# Logic for quotient
# quotient = numerator / denominator
#
# Print the result
# print(f"Quotient is {quotient}.")

''' Let's implement above program using try-except block '''

try:
    # User input on Numerator and Denominator
    numerator = float(input("Enter your numerator: "))
    denominator = float(input("Enter your denominator: "))

    # Logic for quotient
    quotient = numerator / denominator

    # Print the result
    print(f"Quotient is {quotient}.")

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You can't divide by word")
