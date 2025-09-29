"""
Functions in python:

1. In-built functions
2. Module Functions
3. User-Defined Functions

"""

# In-built functions
int()
str()
print()
bool()

# Module functions - Those functions which are imported and have collection of functions

import math
print(dir(math))

''' To import a particular function from module function '''
from math import sqrt
print(sqrt(4)) # Square root of 4 = 2

''' To import all available functions from module function '''
from math import *
print(exp(3))

# User-defined functions - Those are customized/created by user
''' Basic syntax to define functions

def function_name(parameters):
    // do something

'''
# Initialize the function
def print_sum(first, second):
    print(first + second)

# To call/execute above function
print_sum(1, 5)


# Another example of function where if we dont pass any parameters during call.
def print_sum1(first, second = 4):
    print(first + second)
print_sum1(9)
