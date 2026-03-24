''' Inverted Pyramid'''

n = 5

for i in range(1, n + 1):
    # Print spaces
    for j in range(i - 1):
        print(" ", end=" ")
    
    # Print stars
    for j in range(2 * (n - i) + 1):
        print("*", end=" ")
    
    print()


'''Output:
* * * * * * * * * 
  * * * * * * * 
    * * * * *
      * * *
        *
        '''