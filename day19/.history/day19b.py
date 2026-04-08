n = 4
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        val = n - min(i, j, size - i - 1, size - j - 1)
        print(val, end=" ")
    print()


#output:
'''
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4    '''