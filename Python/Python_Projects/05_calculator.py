"""
Calculator Exercise

"""

first = input("Enter first number: ")
operator = input("Enter operator(+,-,*,/,%): ")
second = input("Enter second number: ")

# Convert string data types to int
first = int(first)
second = int(second)

# Calculation Conditions
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid operator")
