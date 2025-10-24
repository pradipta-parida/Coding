"""
Variables in Python:-

Python variable naming rule;
1. Variables names cannot start with numbers
2. Only letters, numbers and underscores(_) can be used
3. Spaces are not allowed in variable names. However, we can use underscores to set apart words
4. Variable names are case-sensitive.
"""

# Rule-1 example

# 3_fav_desserts = ["Cake", "Pie", "Fudge"]
# print(3_fav_desserts)
# O/P: SyntaxError: invalid decimal literal

my_3_fav_desserts = ["Cake", "Pie", "Fudge"]
print(my_3_fav_desserts)

desserts_top_3 = ["Fudge", "Pie", "Pastry"]
print(desserts_top_3)


# Rule-2 example
# Invalid variable syntax are as below;
# my_3_fav_desserts!
# my*3*fav*desserts


# Rule-3 example
# Invalid variable syntax are as below;
# my 3 fav desserts


# Rule-4 example
# Python will recognise below as two different variables;
# my_3_fav_desserts
# My_3_fav_desserts
