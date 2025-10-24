"""
Arithmetic Operators:

+ ----> Sum of two numbers
- ----> Subtraction of two numbers
* ----> Multiplication of two numbers
/ ----> Division of two numbers
// -----> Absolute quotient of two numbers
% ----> Modulus of two numbers/Remainder of two numbers
** ----> Exponentiation of two numbers (power operator)

"""
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Different Arithmetic Operators in python
Sum = a + b
Difference = a - b
Product = a * b
Division = a / b
Division_Absolute = a//b # Also known as Floor Division
Remainder = a % b # Also known as Modulus operator
Power = a ** b

print(f"Sum of a + b = {str(Sum)}")
print(f"Difference of a - b = {str(Difference)}")
print(f"Product of a * b = {str(Product)}")
print(f"Division of a / b = {str(Division)}")
print(f"Absolute Division of a // b = {str(Division_Absolute)}")
print(f"Remainder of a % b = {str(Remainder)}")
print(f"Power of a ** b = {str(Power)}")
