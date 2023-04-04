# Examples of Map and Filter functions:

x = [1, 2, 3, 5, 6, 78, 5, 5, 5, 555, 7, 8, 9, 0]

# This maps every value in 'x' to 'i', performs an operation on it, and returns the result.
mp = map(lambda i: i * 2, x)
print(list(mp))

# Now for Filter operations:

# Filter functions check if the result of the function is True, and returns it in its output if so.
mp = filter(lambda i: i % 2 == 0, x)  # This checks if every value within 'x' is an even number...
print(list(mp))  # ...and returns it if the result is True.


# One can also define a more complex 'persistent' function before performing Map or Filter on that:
def func1(i):  # Taking one argument...
    i = i * 3  # Multiplying 'i' by a random number, in this case 3...
    return i % 2 == 0  # ...and checking if the result is an even number.


mp = filter(func1, x)  # Now we can use Filter on 'func1' instead of defining a lambda for the same result as above.
print(list(mp))