



# LCM using GCD

import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = (a * b) // math.gcd(a, b)
print("The LCM of", a, "and", b, "is", lcm)


'''output:
Enter first number: 20
Enter second number: 4
The LCM of 20 and 4 is 20'''