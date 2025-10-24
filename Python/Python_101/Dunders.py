"""
Dunders in Python:

Whenever we run a file, python automatically creates several variables in the background.
These special variables known as Dunders.(which is short for double underscores, have names enclosed
in double underscores)

__name__
__file__
__doc__
More!

"""

# sample code
# print(__name__)
# O/P: __main__

# Another sample code
print(f'file_1__name__: {__name__}')

if __name__ == '__main__':
    print(f'__name__equals__main__')

'''
But why is name equal to main in the above example?

It actually depends on whether the file is run as a script or imported as a module.
When the file is executed directly as a script. The name variable will always be assigned the value main.
In this example, Dunders.py was run directly as a script, which explains why name equals main.

However files can also be executed indirectly, which happens whenever we import a file as a module.
In this case the name variable will be assigned the module's name. 
'''

# 2nd concept

'''
def add(x+y)
    return x+y

# Test code
if add(1, 2) == 3:
    print("Pass")
else:
    print("Fail")

if __name__ == '__main__':
    print(f'__name__equals__main__')

'''

'''
When we execute Dunders.py the above code runs as intended and the output confirms that the add function works
correctly. Now we can use add function with confidence in any of our other files.
For example, if i like to add two numbers in 30_dunders(2).py , I can use Dunders.py file modules add function
and print the result. (check the code in 30_Dunders.py), but there is an issue here.
Remember, when we import a file as a module python runs the entire file. This means that the test code we wrote in
Dunders.py will be executed during the import statements in 30_Dunders(2).py
'''

# To not execute the sample test code
'''
def add(x+y)
    return x+y
    
if __name__ == '__main__':
    if add(1, 2) == 3:
        print("Pass")
    else:
        print("Fail")
    
 
'''