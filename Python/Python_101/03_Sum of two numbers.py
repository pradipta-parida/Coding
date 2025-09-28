"""

Print sum of two numbers

"""

first = input("Enter First number: ")
second = input("Enter Second number: ")

sum = first + second

# Concatenate of strings
print(sum)

# Sum operations by converting string into int
sum1 = int(first) + int(second)
print(sum1)

# To print sum in concatenate of string we need to convert it from int to string

print("sum of two numbers is: " + str(sum1))