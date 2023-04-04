y = "item"
# This is what is known as a "comprehension":
x = [y for z in range(5)]
print(x)

# This is another example:
# Here, every 'b' is a number within the range of 3; that range is then assigned to 'b'.
# Next, for every 'b' (where each 'b' is now a range of 3) in a range of 6, we store 'b' (a range of 3).
a = [[b for b in range(3)]for b in range(6)]
print(a)

# ...and another example:
d = [d for d in range(3)]
print(d)

e = [i for i in range(100) if i % 2 != 0]
print(e)

# The above example with 'e' is the same as saying:

running_tally = [num for num in range(100) if num % 2 != 0]
# My variable... for every 'thing' in 'range' where the remainder of 'thing' divided by 2 is not 0...
print(running_tally)

numa = [[numb for numc in range(3)]for numb in range(6)]
print(numa)