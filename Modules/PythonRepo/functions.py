# These are examples of Functions...

# The first example is a niche case, demonstrating Python's ability to
# include a shadowed function name nested as another function
# (or a "sub-function", if you will), complete with its own code.
print("\n" + "FUNCTION 1:")


def func1():
    print("Run")

    def func1():
        print("Me")

    func1()


func1()

print("____________________________________________________________________")
# Example 2:
print("\n" + "FUNCTION 2:")


def func2(x, y):
    print(x, y)


func2(2, 3)

print("____________________________________________________________________")
# Example 3:
print("\n" + "FUNCTION 3:")


def func3(a, b, c):
    print("Run", a, b, c)
    return a * b, b / c


r1 = func3(2, 3, 4)
print(r1, type(r1))

r2 = func3(3, 4, 5)
print(r2, type(r2))

r3 = r1 + r2
print(type(r3))
print(tuple(r3), type(r3))

print("____________________________________________________________________")

# An example of Variable Unpacking operations:

x = (1, 2, 3, 4, 5, 6)
print("Let's 'unpack' 'x':")
print(*x)  # The '*' will unpack the items in the list, instead of printing the list.
print("\n" + "Now let's compare the above to simply printing 'x':")
print(x)