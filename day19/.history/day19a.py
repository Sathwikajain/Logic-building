n = 5
for i in range(1, n + 1):
    num = i % 2  # 1 for odd row, 0 for even row  
    for j in range(1, i + 1):
        print(num, end=" ")
        num = 1 - num  # toggle between 0 and 1
    print()

#output:
'''
1 
0 1 
1 0 1
0 1 0 1
1 0 1 0 1 '''   