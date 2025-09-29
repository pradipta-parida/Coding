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
a = float(input("Enter first nubmer: "))
b = float(input("Enter second nubmer: "))

# Different Arithmetic Operators in python
Sum = a + b
Difference = a - b
Product = a * b
Divison = a / b
Dvison_Absolute = a//b
Remainder = a % b
Power = a ** b

print("Sum of a + b = " + str(Sum))
print("Difference of a + b = " + str(Difference))
print("Product of a * b = " + str(Product))
print("Divison of a / b = " + str(Divison))
print("Absolute Divison of a // b = " + str(Dvison_Absolute))
print("Remainder of a % b = " + str(Remainder))
print("Power of a ** b = " + str(Power))
