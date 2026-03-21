'''# Program to calculate sum of digits'''

number = int(input("Enter a number: "))

number = abs(number)  # handle negative numbers
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10

print("Sum of digits:", total)


'''Output:
Enter a number: 89
Sum of digits: 17'''