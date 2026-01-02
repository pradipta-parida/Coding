"""
Data Class - A special kind of class that's designed mostly for holding data
             without writing a lot of the boilerplate code for regular classes.
             They automatically generate: __init__, __repr__, __eq__
"""
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    is_alive: bool = True


person1 = Person("Spongebob", 30)
person2 = Person("Patrick", 35)

print(person1)
print(person2)
print(person1 == person2) # O/P: False

print(person1 == person2) # O/P: True
"""
person1 = Person("Spongebob", 30)
person2 = Person("Spongebob", 30)
"""
