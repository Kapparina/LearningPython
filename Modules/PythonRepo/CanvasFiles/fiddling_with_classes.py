# Object-Oriented Programming - Inheritance

class Pet:  # This is a 'general' or 'upper-level' class.
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

    def speak(self):
        print("I... am confused...")


class Cat(Pet):
    def __init__(self, name, age, colour: str):
        super().__init__(name, age)
        self.colour = colour

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old. I am {self.colour}.")

    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


bob = Cat("Bob", 5, "red")
bob.name = "Bobby"
bob.age = 20
bob.show()
frank = Dog("Frank", 10)
frank.show()