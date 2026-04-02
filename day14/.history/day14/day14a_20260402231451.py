# Reverse number and print in words
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

words = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

print("Output:", end=" ")
while rev > 0:
    digit = rev % 10
    print(words[digit], end=" ")
    rev //= 10

    
    
   output:
    
    Input: 321
    Reversed: 123
Output: One Two Three