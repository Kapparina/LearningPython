# Zip

names = ["John", "Joel", "Frank", "Bob"]
ages = [26, 56, 45, 33]
eye_colour = ["blue", "brown", "green", "hazel"]

for name, age in zip(names, ages):
    if age > 30:
        print(name)

print(list(zip(names, ages, eye_colour)))