# Factorial using recursion

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1    
    # Recursive call
    return n * factorial(n - 1)
n = 5

print("Factorial:", factorial(n))

//