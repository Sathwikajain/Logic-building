arr = [0, 1, 2, 0, 3, 4, 0]
pos = 0 
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
print("After moving zeros:", arr)


#output: