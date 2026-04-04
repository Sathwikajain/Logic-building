# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
found = False
for i in range(2, num):
    if is_prime(i) and is_prime(num - i):
        print(num, "=", i, "+", num - i)
        found = True
if not found:
    print("No combination found")

output:
Enter a number: 34
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17
34 = 23 + 11
34 = 29 + 5
34 = 31 + 3    