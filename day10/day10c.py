# Swapping without temp variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# output:
# Enter first number: 20
# Enter second number: 7
# Before swapping: a = 20 , b = 7
# After swapping: a = 7 , b = 20