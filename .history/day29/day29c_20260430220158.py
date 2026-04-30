# Matrix transpose

A = [[1, 2, 3], 
     [4, 5, 6]]

rows = len(A)
cols = len(A[0])

transpose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    transpose.append(row)

print("Transpose:", transpose)

Transpose: [[1, 4], [2, 5], [3, 6]]