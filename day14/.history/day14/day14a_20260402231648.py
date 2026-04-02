num = int(input("Enter a number: "))
rev = 0

# Step 1: Reverse number
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

words = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}
result = []
while rev > 0:
    digit = rev % 10
    result.append(words[digit])
    rev //= 10

# Reverse list to maintain order
result.reverse()

print("Output:", " ".join(result))