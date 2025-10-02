"""
Break and Continue in Python:

Break - used when we want to discontinue the loop process
Continue - used when we want to exclude one item from the loop to process it

"""

students = ["ram", "shyam", "kishan", "radha", "radhika"]

# Print names upto radha.
# This will exclude printing of "radha"
for item in students:
    if item == "radha":
        break
    print(item) # ram, shyam, kishan

# Print names excluding "kishan"
# This will print all names except "kishan"
for item in students:
    if item == "kishan":
        continue
    print(item) # ram, shyam, radha, radhika
