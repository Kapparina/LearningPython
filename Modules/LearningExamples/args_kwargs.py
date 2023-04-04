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