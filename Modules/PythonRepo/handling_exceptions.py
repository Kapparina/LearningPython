# Examples of exception handling:

# raise Exception("bad")
def func_exception():
    raise FileExistsError("FILENOOOO")  # Call me for a demonstration.


# Now for Try:
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print("finally")