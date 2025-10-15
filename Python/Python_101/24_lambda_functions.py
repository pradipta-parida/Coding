"""
Lambda functions in python:

1. Lambda functions in python can be divided into 3 parts
    Part 1 ---> Keyword (Lambda)
    Part 2 ---> Parameter of lambda function
    Part 3 ---> Lambda function operation

2. Some more important points about lambda functions are as below;
    i. Can have multiple parameters
    ii. Must be written on a single line of code
    iii. Have different syntax from regular functions
    iv. Lambda functions don't have return statements, that's because a lambda function automatically returns the result of its operation
    v. Lambda functions don't have a name (that's why also called as anonymous function)
"""

# Sample lambda function, which squares a given number
# lambda num: num ** 2

# Lambda function having multiple parameters
# lambda num_1, num_2: (num_1 + num_2) ** 2


# Sample example of function, which squares a given number
# def square(num):
#     return num ** 2

# Why use lambda function? And how to call it.
def square(num):
    return num ** 2

def cube(num):
    return num ** 3

# In python, a function that takes another function as an input is called a higher order function.
# In below case, transform_list is the higher-order function which takes input from transform_item function
# In below example, we can transform the first item in our list by calling the transform item function passing the first item as an argument
# To transform the second item in the list, we can call the transform item function again.
# To complete the transform list function, we assign the transform items to variables and return a new list with the transform values
def transform_list(nums_list, transform_item):
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0, transformed_1]

my_list = [2, 3]

# To square the items in my list, we call the transform list function passing in my list and the square function
#print(transform_list(my_list, square))
# To cube the items in my list
print(transform_list(my_list, cube))

