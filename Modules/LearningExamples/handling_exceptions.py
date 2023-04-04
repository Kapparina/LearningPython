# Examples of exception handling:

# raise Exception("bad")
def func_exception():
    raise FileExistsError("FILENOOOO")  # Call me for a demonstration.


# Now for Try:
try:
    x = 7 / 0
except Exception as e:  # This one-liner will print the default exception, in this case 'Division by zero', as a string.
    print(e)
finally:  # This dictates what is to happen at the end of a 'try/except' block.
    print("finally")


print("_____________Time for another example:_______________")


try:
    # value = 10 / 0  # Remove my initial '#' to see the ZeroDivisionError exception being caught.
    number = int(input("Enter a number: "))
    print("Your number is", int(number))
except ZeroDivisionError:  # Here we've incorporated a way to catch two types of errors...
    print("Divided by zero")
except ValueError:  # ...here is the second type of error able to be caught by this one 'try/except' block.
    print("Invalid input")