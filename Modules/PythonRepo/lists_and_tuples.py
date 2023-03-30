# Example of list with For loop:

x = [1, 2, 3, 4]
y = x[:]
print(x.pop(), x)
print(y)
for num, element in enumerate(x):
    print(num, element)

# Example with While loop:

i = 0
while True:
    print("hey this is an example of a while loop", i)
    i += 1
    if i == 10:
        break