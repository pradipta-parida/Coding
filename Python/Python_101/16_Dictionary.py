"""
Dictionary in python:

1. We store  [key:value] pairs in dictionary
2. Here, we use {} to initialize the dictionary

"""

# Initialize dictionary using {}
marks = {"english" : 95, "chemistry" : 85, "mathematics" : 85}

# To print any value of a key
print(marks["chemistry"])

# To append a new key-value pair in our existing dictionary and then print the new dictionary
marks["physics"] = 97
print(marks)

# To modify value of a key in a dictionary
marks["physics"] = 99
print(marks)
