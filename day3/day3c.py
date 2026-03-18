# Program to find quotient and remainder

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

if divisor == 0:
    print("Division by zero is not allowed")
else:
    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Quotient:", quotient)
    print("Remainder:", remainder)


#output:
# Enter dividend: 4
# Enter divisor: 2
# Quotient: 2
# Remainder: 0