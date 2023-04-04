# Example of list with For loop:

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = x[:]

print("This prints the last indexed value of the 'x' list:")
print(x.pop(), x)

print("This prints the value of the 'y' list, which is the 'x' list prior to being 'popped':")
print(y)

print("This prints the values within the 'x' list alongside each values' index:")
for num, element in enumerate(x):
    print(num, element)

print("____________________________________________________________________")
# Example with While loop:

i = 1
while True:
    print("This is an example of a while loop, which has run", i, "out of 10 times")
    i += 1
    if i == 11:
        break

print("____________________________________________________________________")
# Example of Slice operator:

slicer = x[0:6:2]
print("This prints from one value to another within a list or range, stepping a specified number between each:")
print(slicer)

print("____________________________________________________________________")
# Examples of Sets:

s1 = {1, 2, 3, 55, 4, 4, 0}
s2 = {"a", "b", "c", "d", 9, "x", "y"}
print("This prints the contents of set 's1':")
print(s1)

print("...and this prints the contents of 's1' after being combined with '2':")
print(s1.union(s2))

print("____________________________________________________________________")



