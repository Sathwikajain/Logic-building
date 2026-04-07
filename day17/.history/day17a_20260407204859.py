# Binary to Decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
binary = input("Enter a binary number: ")
print("Decimal equivalent:", binary_to_decimal(binary))

