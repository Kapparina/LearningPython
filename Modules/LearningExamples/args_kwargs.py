# This contains examples of *args and **kwargs:

# Observe below, a function where *args and **kwargs would be used:
def func(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(pair[0], pair[1])

print("\n" + "Now let's see the function's output with *args:")
for pair in pairs:
    func(*pair)

print("The same, but neater and with less code...")

print("\n", "Let's see another example:")


def func1(a, b, c):
    print(a, b, c)


args = ["This", "totally", "works"]
func1(args[0], args[1], args[2])  # I can do this...
func1(*args)  # Or I can use '*args' to do this for me.

print("\n", "Now for more:")


def func2(arg1=None, arg2=None, arg3=None, arg4=None):
    print(arg1, arg2, arg3, arg4)


kwargs = {"arg2": 2, "arg1": 1, "arg3": 3, "arg4": 4}
print("'kwargs' is a:", type(kwargs), "object")

func2(*kwargs.items())  # I can do this to expand the whole dictionary using the function.
func2(**kwargs)  # I can also use '**kwargs', which will both take my dictionary values and order them.
