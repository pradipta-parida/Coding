"""

If-else Statements:

When condition satisfies then Print or execute (if) statement
When (if) condition doesn't satisfy then Print or execute (elif) statement. And multiple (elif) conditions can be present in a code.
When none of the condition (if or elseif) satisfies then Print or execute (else) statement

(elif) condition will be executed if the above conditions does not satisfy.
(if) conditions are only there then, it will check all conditions, which take some processing time.
"""

age = int(input("Enter age: "))

if age >= 18:
    print("You are an adult")
    print("You can vote")

elif age < 18 and age > 3:
    print("You are in school")

else:
    print("You are a child")
