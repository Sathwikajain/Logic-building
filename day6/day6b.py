'''# Right-angled Triangle'''
n = 5
for i in range(1, n + 1):      # rows
    for j in range(i):         # stars increase
        print("*", end=" ")
    print()

'''output:
* 
* * 
* * *
* * * *
* * * * *'''