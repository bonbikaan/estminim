from collections import namedtuple

# Create a namedtuple class called 'Person' with fields 'name' and 'age'
Person = namedtuple('Person', ['name', 'age'])

# Create an instance of the Person class
person1 = Person(name='Alice', age=30)

# Access the fields of the instance
print(person1.name)  # Output: 'Alice'
print(person1.age)   # Output: 30
