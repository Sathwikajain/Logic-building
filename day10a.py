# Pattern 1
n = 5
for i in range(1, n + 1):
    char = chr(65 + i - 1)
    
    for j in range(i):
        print(char, end=" ")   
    print()
# output:
# A 
# B B 
# C C C
# D D D D
# E E E E E