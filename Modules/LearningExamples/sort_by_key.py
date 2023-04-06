# Sort by key

lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]  # Here I have a list.

print("Let's sort the list using the 'sort()' method:")
lst.sort()  # I could sort the list by the first item in each sub-list in place...
print(lst)

print("\n" + "Now let's sort it with the 'sort()' method with the 'reverse' flag:")
lst.sort(reverse=True)  # ...I could reverse the sorting order with the 'reverse' flag...
print(lst)

print("\n" + "Now let's pass the 'sort()' method a function containing the first index of each item:")


def sort_func0(x):
    return x[0]


lst.sort(key=sort_func0)
print(lst)

print("\n" + "Now we'll do the same, instead passing the 'sort()' method a function with the second index:")


def sort_func0(x):
    return x[1]


lst.sort(key=sort_func0)
print(lst)

print("\n" + "Now we'll pass 'sort()' the first index plus the second index (the sum of each), using a function:")


def sort_func1(x):  # This is how one would perform the above operation without 'lambda'.
    return x[0] + x[1]


lst.sort(key=sort_func1)  # Calling the function as the key for the 'sort()' method.
print(lst)

print("\n" + "Finally, we'll pass 'sort()' that same sum via 'lambda', allowing us to omit the function entirely:")
lst.sort(key=lambda x: x[1] + x[0])  # 'lambda' here basically says 'x is temporary for this expression'.
print(lst)
