"""
Nested Loops in Python:-

1. Example of for loop header;

    for number in numbers:
"""

# Sample loop example
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# To print on the same line, we use end keyword
for number in numbers:
    print(f"{number}{letters[0]}", end=" ")
    print(f"{number}{letters[1]}", end=" ")
    print(f"{number}{letters[2]}", end=" ")
    print()

# O/P:
# 1a 1b 1c
# 2a 2b 2c
# 3a 3b 3c


''' To simplify our code, instead of writing repeated lines of print statements, we use nested loop'''
for number in numbers:
    for letter in letters:
        print(f"{number}{letter}", end=" ")
    print()

"""
How nested loops work:

Python starts by executing the outer for loops header and sets the number iteration variable equal to one.
The first item in the numbers list next python moves into the outer loops body and executes the inner loops header.
Here, python sets the letter iteration variable equal to a , which is the first item in the letters list.
Then python moves into the inner for loops body and prints the number and letter variables. At this point the number
variable is one and the letter variable is a. So, python prints 1a in the output box. Since this is the last line of the
inner loop, python returns to the header of the inner loop. Python will execute all iterations of the inner loop before
continuing with the rest of the outer loop's body.
In the second iteration, it updates letter to b and prints 1b and in the third iterations it updates the letter to c
and prints 1c.
After the third iterations, python return to the inner loop header. Since there are no more letters in the letters list
, python moves to the final print statement in the outer loop. At this point python has completed one iteration of the 
outer loop and three iterations of the inner loop
The second iteration of the outer loop works just the same as the first except now the number variable is assigned the
value 2. This means that when python executes the inner loop every grid entry that is printed will start with 2.....
"""

"""
When to use nested loops?

- Multi-dimensional data

1. Example a student spread-sheet having students name and marks
 
 for student in students:
    total = 0
    for score in scores:
        total += score
    print(total)
    
2. Example image processing: pixel color

 for row in rows
    for column in columns:
       greyscale(row, column)

"""



