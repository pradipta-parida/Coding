"""
Python Dictionaries:

1. There is a python structure that works like a real dictionary.
2. When you look up a word or a key, you get its definition or value
3. To create a python dictionary, we start with curly brackets in between
   those brackets we write the dictionary entries
4. Two parts of dictionary entries: Key-value pairs
5. The key is the label we want to use to access the value. key ---> value
6. When a dictionary has more than one entry than we separate them with commas ,
"""

# Sample Dictionary
# In below example, Key is 'Bob' and his value is the 'email_address'
# Assign the below dictionary to variable contacts
contacts = {
    'Bob' : 'bob@yahoo.com',
    'Wendy' : 'ilovebirds@gmail.com',
    'Cecilia' : 'ilovecats@yopmail.com'
}

# To retrieve Bob's email address from dictionary. We follow the name of our dictionary with square brackets
# we put the key which we are looking for
print(contacts['Bob'])

# Sample list
contacts = [
    'bob@yahoo.com',
    'ilovebirds@gmail.com',
    'ilovecats@yopmail.com'
]

# What's the major drawback of list over dictionary
"""
The major difference b/w dictionary and list lies in how the values are identified.
In a list the items are identified or indexed by their position in the list.
For example, if we want to bet Bob's email address we need to remember that its the first item in the list.
and index that list with zero. That's reasonable with three items in above contact list. But if we have a
lot of items in a list then remembering the position of each items in the list will be very hard.

But with a dictionary we only need to remember the first item(key) in the list, to get their emails.

Few use cases of dictionaries;
Products-prices, Username-passwords, Students-grades  
"""

#Dictionary - Key and value rules
"""
1. Values of dictionary can be of any data type
2. Multiple keys can have the same value
3. Keys must be unique
4. Keys in a dictionary don't need to be strings
"""

# Example of Rule no.1
siblings = {
    'Bob' : 3,
    'Wendy' : 1,
    'Cecilia' : 2
}

# Example of Rule no.2, where Bob and Cecilia keys have same False value
has_pet ={
    'Bob' : True,
    'Wendy' : False,
    'Cecilia' : False
}

# Example of Rule no.3, where
contacts = {
    'Bob' : 'bob@yahoo.com',
    'Wendy' : 'ilovebirds@gmail.com',
    'Cecilia' : 'ilovecats@yopmail.com',
    'Wendy' : 'ilovebirds@outlook.com'
}
'''
o/p:-
    'Bob' : 'bob@yahoo.com',
    'Wendy' : 'ilovebirds@outlook.com',
    'Cecilia' : 'ilovecats@yopmail.com'
'''
# So, how do python know which email to return. The answer is the latest value of the key.

# How to modify an existing dictionary, by adding or removing entries
'''
For example, we want to add Alex - coolalex@gmail.com
'''
contacts['Alex'] = 'coolalex@gmail.com'
print(contacts) # To print dictionary contents
# O/P: {'Bob': 'bob@yahoo.com', 'Wendy': 'ilovebirds@outlook.com', 'Cecilia': 'ilovecats@yopmail.com', 'Alex': 'coolalex@gmail.com'}

# To remove key-value pairs we can use pop method.
'''
For example, we want to remove wendy. Then, pass the key (wendy)
'''
contacts.pop('Wendy')
print(contacts)
# O/p: {'Bob': 'bob@yahoo.com', 'Cecilia': 'ilovecats@yopmail.com', 'Alex': 'coolalex@gmail.com'}

# Dictionary Methods
"""
.keys() -> to return all the keys in the dictionary
"""
print(contacts.keys())
# O/P: dict_keys(['Bob', 'Cecilia', 'Alex'])
# Note: the above keys are wrapped inside a dictionary keys object.
# When we use a for loop, we can iterate over this type of object just like we would with a list.

# To check if 'Alex' is in our contacts without printing the whole dictionary, we can write a for loop that iterates through the keys

for kiy in contacts.keys():
    if kiy == 'Alex':
        print("Alex is in contacts !!!")

# To check if 'bob@yahoo.com' is present in our dictionary without printing the whole dictionary
"""
.values() --> to return all the values in the dictionary
"""
print(contacts.values())
# O/P: dict_values(['bob@yahoo.com', 'ilovecats@yopmail.com', 'coolalex@gmail.com'])

# To check if 'bob@yahoo.com' is present in our dictionary, we write a for loop that iterates through the values.

for value in contacts.values():
    if value == 'bob@yahoo.com':
        print("Email found")

# But what if we need both key and value at the same time.
# For example, to figure out whose email is 'bob@yahoo.com'
"""
.items() method

The items method return the key and value pairs at the same time as tuples
"""
contacts.items()
print(contacts.items())
# O/P: dict_items([('Bob', 'bob@yahoo.com'), ('Cecilia', 'ilovecats@yopmail.com'), ('Alex', 'coolalex@gmail.com')])

for key, value in contacts.items():
    if value == 'bob@yahoo.com':
        print(value, "->", key)

