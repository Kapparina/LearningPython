# Object-Oriented Programming - Dog Example

class Dog:  # This is defining a class of object named "Dog".

    # 'self' is used to denote the object itself.

    # If 'self' is not present when a method is defined, any use of the method will fail with the following error:
    # 'Type Error: <method> takes 0 positional arguments but <number> was given.'

    # The reason this occurs is that every time a method is used on a 'Dog' class object, the object (or 'Dog') name
    # is invisibly passed into the 'self' variable for the purposes of identifying which 'Dog''s attributes are
    # to be retrieved.

    # If you don't include 'self' in a method...

    #   def bark(): <-- Notice the lack of 'self' within these parentheses.
    #       print("bark")

    # ...and attempt to tell a 'Dog' named 'Darren' (in this example let's pretend we have access to the __init__ method
    # present in this file's code) to bark:

    #   d = Dog("Darren")
    #   d.bark()

    # The program will fail.
    # One way to think about this principle is this:
    # When you tell a 'Dog' named 'Darren' to bark, 'self' can be thought of as being substituted for 'Darren' or 'd':

    #   class Dog: <-- Defining a class of object known as 'Dog'.

    #       def __init__(self, name): <-- Upon instantiation of a new 'Dog', it is to be named.
    #           self.name = name

    #       def bark(self): <-- Notice the use of 'self' here.
    #           print("bark")

    #   d = Dog("Darren") <-- An instance of a 'Dog' class object, known as 'd', has been attributed the name 'Darren'.
    #   d.bark() <-- When we use the 'bark' method on 'd', we are substituting the 'self' in the method with 'd'.

    # In order to substitute 'self' with 'd' in the above example, 'self' must exist to be substituted, else the method
    # will not be able to identify which 'Dog' class object is being referred to; 'self' can therefore be thought of
    # as a placeholder. See below:

    #   d.bark()

    # could be seen as, if we apply context to the 'bark' method being called:

    #   def bark(d): <-- While you may never see this, the method can be seen as having substituted 'self' for 'd'.
    #       print("bark")

    def __init__(self, name, age):  # Upon instantiation of a 'Dog', we can name it and give it an age.
        self.name = name  # This is an attribute, which will be applied to an instantiated 'Dog'.
        self.age = age

    def get_name(self):  # This method can be used to retrieve the name of a 'Dog'.
        return self.name

    def get_age(self):  # This method can be used to retrieve the age of a 'Dog'.
        return self.age

    @staticmethod
    def add_one(x):  # This method is used to demonstrate the versatility of custom-defined methods.
        return x + 1

    def bark(self):  # This method starts to define the operations able to be performed by a 'Dog'.
        print("bark")  # Here we can see that a 'Dog' is able to 'bark'.

    def set_age(self, age):  # This method takes a variable...
        self.age = age  # ...and modifies the 'age' attribute defined above, changing the corresponding value of 'age'.


d = Dog("Fido", 12)  # This instantiates a 'Dog' attributed the 'name' 'Darren' and the 'age' '12'.

d.bark()  # Here we take our 'd' object and use the 'bark' method, defined in our class 'parameters', on it.

print(d.add_one(5))  # This passes a value of '5' to the 'add_one' method, which returns a result.

print(type(d))  # Here we print the type attributed to 'd'.

print(d.get_age())  # We retrieve the 'age' attribute of 'd' and print it...
d.set_age(10)  # ...we alter the 'age' attribute of 'd'...
print(d.get_age())  # ...before finally printing the newly attributed 'age' of 'd'.

# While one could use a list of 'name' and 'age' attributes to achieve the same result as defining a class, as below:

#   dog_names = ["Fido", "Boris", "Pluto"]
#   dog_ages = [12, 10, 7]

# Referring to each 'dog' in this context would require checking the index of each 'dog' in each list.
# Removing a 'dog' would entail removing the item at each index of each list.
