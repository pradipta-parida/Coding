"""
F-string or Formatted string:

A formatted string, or f-string, in Python is a type of string literal that makes it easy to embed variables,
expressions, and even function calls directly into strings by enclosing them in curly braces {} and prefixing the string with f. F-strings were introduced in Python 3.6 and are now considered the modern, efficient way to perform string formatting.

Syntax and Basic Example
To use an f-string, prefix the string with the letter f and include any variable or expression inside curly braces.

Example:

python
name = "Alice"
age = 30
print(f"Hello, {name}. You are {age} years old.")

O/P: Hello, Alice. You are 30 years old.
"""

# Sample code
f_temp = 67

# Hard coding the value. It's not best practice.
"The temperature is 67 degrees fahrenheit"

# Instead, we like to embed the value of f_temp directly in the string.
# This is easy to do with an f-string.
# Next, the embedded part should be in curly braces {}
f"The temperature is {f_temp} degrees celsius"

# Suppose,we want to convert the temp to Celsius
temp = f"The temperature is {(f_temp-32)/1.8} degrees celsius"
print(temp)
# O/P: The temperature is 19.444444444444443 degrees celsius

# Rounding with f-strings
# To round the decimal to two places in f-string
# To format the decimal places in the expression, we write a period .
# the number of decimal places we want to display one, and the letter f to display the result as a float
temp = f"The temperature is {(f_temp-32)/1.8:.1f} degrees celsius"
print(temp)

# To round two-decimal places
temp = f"The temperature is {(f_temp-32)/1.8:.2f} degrees celsius"
print(temp)

'''
But why we need to write f after the number of places.
Well because f strings offer flexible ways to display decimal numbers in multiple ways and float is just one way.
For example, we could instead display the results in scientific notation by replacing f with e
'''
temp = f"The temperature is {(f_temp-32)/1.8:.2e} degrees celsius"
print(temp)

'''
or we could format the value as a percentage using a percent sign
'''
temp = f"The temperature is {(f_temp-32)/1.8:.2%} degrees celsius"
print(temp)


# Big numbers with f-strings
'''
To improve readability of large numbers.
'''
f_temp_sun = 27000000
sun_temp = f"The temperature is {(f_temp_sun-32)/1.8:.2f} degrees Celsius"
print(sun_temp)

# f-strings allows us to add comma separators
f_temp_sun = 27000000
sun_temp = f"The temperature is {(f_temp_sun-32)/1.8:,.2f} degrees Celsius"
print(sun_temp)


# More formatting with f-strings
'''
It provides the flexibility to control the spacing, alignment and padding around our expression.
'''
f_temp_sun = 27000000
f_temp_earth = 58

print(f"The temperature is {(f_temp_sun-32)/1.8:,.2f} degrees Celsius")
print(f"The temperature is {(f_temp_earth-32)/1.8:,.2f} degrees Celsius")
# O/P: The temperature is 14,999,982.22 degrees Celsius
#      The temperature is 14.44 degrees Celsius


# Above result is a bit messy since the results take up different amount of space.
# To fix that, f-strings lets us control the space that a result will take up as below;
#  :[width],.[decimals][type]

f_temp_sun = 27000000
f_temp_earth = 58

print(f"The temperature is {(f_temp_sun-32)/1.8:15,.2f} degrees Celsius")
print(f"The temperature is {(f_temp_earth-32)/1.8:15,.2f} degrees Celsius")
#o/p: The temperature is   14,999,982.22 degrees Celsius
#     The temperature is           14.44 degrees Celsius


# To fix the alignment up as below;
# [alignment]:[width],.[decimals][type]
# Below is the left-align format, append <
print(f"The temperature is {(f_temp_sun-32)/1.8:<15,.2f} degrees Celsius")
print(f"The temperature is {(f_temp_earth-32)/1.8:<15,.2f} degrees Celsius")

# If we want the values to sit in the center of the 15 characters, we can use the carrot symbol
print(f"The temperature is {(f_temp_sun-32)/1.8:^15,.2f} degrees Celsius")
print(f"The temperature is {(f_temp_earth-32)/1.8:^15,.2f} degrees Celsius")
# O/P: The temperature is  14,999,982.22  degrees Celsius
# The temperature is      14.44      degrees Celsius


# Now you might have noticed when the value doesn't take up the full width, something fills in the extra space
# By default, those leftover spots are filled with space characters. But we are not limited to spaces.
# We can choose a different character instead as below;
# [fill][alignment]:[width],.[decimals][type]
print(f"The temperature is {(f_temp_sun-32)/1.8:*^15,.2f} degrees Celsius")
print(f"The temperature is {(f_temp_earth-32)/1.8:*^15,.2f} degrees Celsius")
