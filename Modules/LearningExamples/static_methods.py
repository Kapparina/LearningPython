# Object-Oriented Programming - Static Methods

class Math:

    @staticmethod  # This is a static method. A static method is a method housed within a class not acting on the class.
    def add5(x):
        return x + 5

    @staticmethod  # A static method accepts variables, but doesn't need them like instance or class methods.
    def pr():
        print("run")

Math.pr()  # Notice here the 'pr' static method has been called on the 'Math' class.