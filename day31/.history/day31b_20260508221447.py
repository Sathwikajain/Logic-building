# Power using recursion

def power(base, exponent):
    
    # Base case
    if exponent == 0:
        return 
    return base * power(base, exponent - 1)
base = 2
exponent = 3

print("Result:", power(base, exponent))