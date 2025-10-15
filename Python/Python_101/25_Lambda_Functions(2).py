"""
Best use of lamda function on above function.

Built-in higher order function;
    1. map() --> works a lot like transform_list function, except it can take a list of any length and apply an operation to each item.
    2. filter() --> works a lot like map(), but instead of transforming items in a list, it only keeps items that meet a condition
"""

# def transform_list(nums_list, transform_item):
#     transformed_0 = transform_item(nums_list[0])
#     transformed_1 = transform_item(nums_list[1])
#     return [transformed_0, transformed_1]
#
# print(transform_list([2, 3], lambda num: num ** 3))

'''Using map()'''
nums_list = [2, 3, 4, 5, 6]

# We call map and pass two arguments. First, a function that takes a number and return its cube.
# And second, a list of numbers.
# Here, we cast map to list as below.
print(list(map(lambda num:  num ** 3, nums_list)))


'''Using filter()'''
# Using above nums_list to keep even numbers only.
# To do this, we need two arguments. First a lambda function that takes a number and checks the condition.
# If the condition satisfies True: Number is even & included in final list
# If the condition satisfies False: Number is odd & not included in final list
# Second, we pass the list of numbers.
# Just like the map we need to cast the result to a list
nums_list = [2, 3, 4, 5, 6]
print(list(filter(lambda num: num % 2 == 0, nums_list)))

