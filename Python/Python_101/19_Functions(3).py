""" Namespaces - A namespace is like a notebook where Python writes down variable names and their current values
                 during execution
"""
'''
Variables created outside of any function like our unit variable (see below code) get placed in what is called a global namespace.
Variables living in global namespace are called global variables.

During function calls, python creates a new temporary namespace called a Local namespace.
Python uses this namespace to store the functions parameters and any variables defined inside it.
Variables living in the local namespace like length, width and area are called local variables.
When a function finishes executing and returns to the calling point, its local namespace is always destroyed.
This means that the variables stored in the local name space are no longer available after the programs return to the calling point.
That's why when we tried to print the area variable outside the function, we got an error saying that area doesn't exist.
Unlike global variables, local variables are temporary.They only exist during a function call.
'''

'''

unit = "feet squared"
def calc_rect_area(length, width):
    area = length * width

calc_rect_area(14, 10)
print(area, unit)

'''
#O/P: NameError: name 'area' is not defined

'''
So, to fix this.
To display the calculated area while following the single-responsibility principle,
we need to return the area back to the main program before the local namespace is destroyed.
We can do this by the use of Return statement.

A return statement starts with a keyword 'return' followed by the variable whose value we'd like to
return to the main program. 
'''

'''
unit = "feet squared"
def calc_rect_area(length, width):
    area = length * width
    return area

calc_rect_area(14, 10)
print(area, unit)
'''
# O/P: NameError: name 'area' is not defined

'''
During the execution of above code,
when python executes the return statement, the value of area is returned back to the calling point: calc_rect_area(14, 10)
before the local namespace is discarded.
In practice, this means that the function call: calc_rect_area(14, 10) expression evaluates the return value 140.
To keep using the return value in the rest of our program, we need to capture it in a variable.
Otherwise the value will be lost once the program continues to the next line.

For example, we can capture 140 by assigning to a new variable called my_area.
This creates a global variable containing 140. This time it should not throw any error.

Note:- We could capture the return value using any variable name. It doesn't need to match the
name of the local variable returned by the function.
'''
unit = "feet squared"
def calc_rect_area(length, width):
    area = length * width
    return area

my_area = calc_rect_area(14, 10)
print(my_area, unit)
