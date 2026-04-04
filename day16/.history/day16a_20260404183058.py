# Palindrome number check
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if rev == num:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
    
    Output:
    