"""
Dunders contd:

"""

print(f'file_2 __name__: {__name__}')


# Dunders imported as module
import Dunders

'''
Note: That when a file is imported as a module, python automatically executes it.
So, running 30_Dunders(2).py will implicitly trigger the execution of Dunders.py

Lets trace the code to see how this works;
30_Dunders(2).py starts by printing the value of the name variable.
Because we are directly running 30_Dunders(2).py . 30_Dunders(2).py --> name is equal to main.
Then we import Dunders.py which triggers the execution of Dunders.py.
As we know Dunders.py starts by printing the value of the name variable.
Since, Dunders.py is being run as a module from 30_Dunders(2).py. 
Dunders.py name variable is no longer assigned the value main.
Instead its assigned, Dunders.py which is the name of the module.
As a result the conditional that tests whether name is equal to main evaluates to false and its body is skipped.

'''

# To sum up we will get below output if we run 30_Dunders(2).py
#O/P: file_2__name__:__main__
#O/P: file_1__name__: Dunders
# And no output from the last print statement

# 2nd concept

'''
We use this as a testing/debugging code in a file that we use as a module
'''


'''
import Dunders

print(Dunders.add(1, 2)) # Use case code

O/P: Pass
      3
'''


'''
As you can see, python first ran the test code in Dunders.py and then executed the add function but we don't really
want file one's test code to run when we execute 30_Dunders(2).py because these tests aren't relevant to how
30_Dunders(2).py uses the function.
It would be much better if the test code only ran when we executed Dunders.py directly as a script.

Luckily, this is exactly what the if __name__ == '__main__': statement in Dunders.py allows us to do.
We can prevent the test code from running when file one is used as a module by moving the test code inside
if __name__ == '__main__': block in Dunders.py

When the Dunders.py run directly the test still executes(O/P: Pass) but now when we run 30_Dunders(2).py, we only get the 
add function result as output not the test result using the if name equals main syntax. (O/P: Pass).

Using the if __name__ == '__main__': syntax in Dunders.py is a clean and simple way to separate use case code from test
case code. It prevents test code from running when a file is imported as a module. The syntax is great for adding quick 
and simple test cases to verify that your module works as expected. However, if your testing needs are more advanced, you should
consider using a proper testing framework like unittest or pytest
'''
