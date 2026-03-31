# GCD using loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("The GCD of", a, "and", b, "is", gcd)


Output:
Enter first number: 2
Enter second number: 4
The GCD of 2 and 4 is 2