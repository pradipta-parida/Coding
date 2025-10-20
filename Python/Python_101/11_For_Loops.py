"""

For loops in python:
To execute a sequence within a range

"""


"""
A for loop begins with a keyword (for). This keyword tells python that we want to repeat some actions for 
multiple items. We follow the for keyword with a variable name of our choice. Programmers often call this variable the
loop or iteration variable. During the execution of the loop, this variable will be sequentially assigned each item in
the collection, we want to iterate through.

Below is called for-loop header and below the header we write indented code that will run for each item.

for <my_var> in <data_collection>:

Since the iteration variable will hold individual price values

"""
# Sample code to print discount
discount = 0.10
prices = [12.99, 15.99, 7.99, 27.99]

for price in prices:
    print(price * (1-discount))
print("Prices Discounted!")

# Another for loop example
ticket_numbers = [0, 1, 2, 3, 4, 5]
for ticket_number in ticket_numbers:
    print("Summer's super raffle")
    print("Ticket number:", ticket_number)

# To print more numbers like 100 in a list we need to write numbers upto 100.
# To avoid this, we introduced range
'''
Python has a built-in function that can generate sequential numbers for us.
This built-in function is called as range. 
'''
for number in range(10): # start at 0 and stop at 9
    print(number)

for number in range(106): # start at 0 and stop at 105
    print(number)

# For loop using lower boundary value
print()
for item in range(1000, 1006):
    print(item)
