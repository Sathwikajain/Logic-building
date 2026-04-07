# Decimal to Binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2
    return binary
num = int(input("Enter a decimal number: "))
print("Binary equivalent:", decimal_to_binary(num))

