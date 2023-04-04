number_grid = [
    [1, 2, 3],  # Each of these rows is literally treated as a row.
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:  # This is a nested For loop.
    for col in row:
        print(col)