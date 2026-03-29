# Program to find the larger number between two numbers

# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Comparing numbers
if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal")