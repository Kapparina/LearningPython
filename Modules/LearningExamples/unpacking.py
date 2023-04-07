tup = (1, 2, 3, 4)

lst = ["Me", "List", 3, 4]

string = "hello"

dic = {"a": 1, "b": 2}

coords = [4, 5]

a, b, c, d = tup
print(f"Unpacking 'tup': {a, b, c, d}")

e, f, g, h = lst
print(f"Unpacking 'lst': {e, f, g, h}")

i, j = dic.items()
print(f"Unpacking 'dic' items: {i, j}")

k, l = dic.values()
print(f"Printing 'dic' values: {k, l}")

m, n = dic
print(f"Printing 'dic' keys: {m, n}")

o, p = coords
print(f"Unpacking 'coords': {o, p}")

q = string
print(f"Unpacking 'string': {q}")