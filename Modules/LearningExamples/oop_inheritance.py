# Object-Oriented Programming - Inheritance

class Pet:  # This is a 'general' or 'upper-level' class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

    def speak(self):
        print("I... am confused...")


class Cat(Pet):  # This is a class of 'Pet', inheriting general attributes, such as 'name' and 'age'.
    def __init__(self, name, age, colour):  # This will be passed up to the parent class by the below line.
        super().__init__(name, age)  # 'super()' refers to the 'super' (or parent) class, and '__init__' that method.
        self.colour = colour

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old. I am {self.colour}.")

    def speak(self):
        print("Meow")


class Dog(Pet):  # This is another class of 'Pet', inheriting general attributes, such as 'name' and 'age'.
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Jim", 19)  # Instantiates a 'Pet' class object - note that it isn't a 'Dog' nor is it a 'Cat'.
p.show()
p.speak()  # Notice that as this is a 'Pet' class object, no child-class method will override it.

c = Cat("Bob", 12, "brown")  # Instantiates a 'Cat' class object, inheriting 'Pet' attributes, and passing unique ones.
c.show()
c.speak()  # Here we have the 'Cat' class object speak - this will return a 'Cat' specific result.

d = Dog("Boris", 15)  # Instantiates a 'Dog' class object, inheriting generalised attributes, such as 'name' and 'age'.
d.show()
d.speak()  # Here we have the 'Dog' class object speak.

f = Fish("Bubbles", 5)  # Here we instantiate a 'Fish' class of object.
f.show()  # The 'Fish' class object knows its 'name' and 'age' because those are inherited (or 'advised') within 'Pet'.
f.speak()  # The 'Fish' class object is confused, because it has no method by which to 'speak'; 'Pet' has it say so.

# A note on how child class methods interact with matching parent class methods:

# If a parent (or 'upper-level') class contains a method with the same name as one present in a child (or 'lower-level')
# class, objects belonging to the child class - and inheriting methods from the parent class - will opt to use the
# methods present within their child class; children succeed their parents.

# In the above example, the 'Dog' and 'Cat' class objects are not confused, and know to 'Bark' and 'Meow' because
# despite the 'speak' method also existing within the parent 'Pet' class, the methods by which they 'speak' have been
# defined within their own child ('lower-level') classes respectively.

# Further to this, if a lower-level (or 'child') class does not contain a method (for example, 'speak'), and that
# method is used on an object within a lower-level class, the object could effectively be seen as 'asking its parent'
# how to do something. In the above code, if the 'Fish' class object, belonging to the parent 'Pet' class of objects,
# does not know how it should 'speak' as determined by its own child class of 'Fish', it will become confused.
