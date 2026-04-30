# Search element in matrix

A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

target = 5
found = False

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == target:
            print("Position:", (i, j))
            found = True
            break
    if found:
        break

if not found:
    print("Element not found")