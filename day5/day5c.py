'''# Program to find ASCII value'''

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter a single character")
else:
    ascii_value = ord(char)
    print("ASCII value of", char, ":", ascii_value)

'''Output:
Enter a character: t
ASCII value of t : 116'''

