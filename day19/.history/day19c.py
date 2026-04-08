n = 5
for i in range(n):
    start = 65 + (n - i - 1) 
    for j in range(i + 1):
        print(chr(start + j), end=" ") 
    print()


#output:
''' 
E 
D E 
C D E
B C D E
A B C D E  '''  