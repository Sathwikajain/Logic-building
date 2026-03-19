'''Simple calculator'''

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print(num1, "+", num2, "=", num1 + num2)

elif operator == '-':
    print(num1, "-", num2, "=", num1 - num2)

elif operator == '*':
    print(num1, "*", num2, "=", num1 * num2)

elif operator == '/':
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        print(num1, "/", num2, "=", num1 / num2)

else:
    print("Invalid operator")

# output:
# Enter first number: 4
# Enter operator (+, -, *, /): *
# Enter second number: 8
# 4.0 * 8.0 = 32.0