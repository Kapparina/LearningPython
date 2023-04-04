# Object-Oriented Programming - Class Attributes

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod  # This is a class method.
    def total_people(cls):
        return cls.number_of_people

    @classmethod  # A class method is bound to the class, and only accepts class variables.
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("John")
p2 = Person("Bob")

print(Person.total_people())