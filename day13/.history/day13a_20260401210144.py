''' LCM using loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = max(a, b)
while True:
    if max_num % a == 0 and max_num % b == 0:
        lcm = max_num
        break
    max_num += 1
print("The LCM of", a, "and", b, "is", lcm)'''



# LCM using GCD

import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = (a * b) // math.gcd(a, b)
print("The LCM of", a, "and", b, "is", lcm)