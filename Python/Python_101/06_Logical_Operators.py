"""

Logical Operators:

OR ---> If any one condition is True then output will be True. If both conditions is False then output will be False. (Addition Analogy)
AND ---> If both conditions is True then output will be True. If any one condition is False then output will be False. (Multiplication Analogy)
NOT ---> If the conditions is True then output will be False and vice versa. (Inverse Analogy)

"""

# Here, first operation would return False and second operation would return True.
# So, Result of OR operation would be True
print(2 > 3 or 2 > 1)

# Here, first operation would return True and second operation would return True.
# So, Result of AND operation would be True
print(3 > 2 and 2 > 1)

# Here, first operation would return True and second operation would return False.
# So, Result of AND operation would be False
print(3 > 2 and 2 > 6)

# Here, first operation is False.
# Due to NOT operator its value gets inversed to False
print(not 3 > 3)

# Here, first operation is True.
# Due to NOT operator its value gets inversed to False
print(not 3 > 2)
