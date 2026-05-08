# Power using recursion

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
base = 2
exponent = 3
print("Result:", power(base, exponent))

#output