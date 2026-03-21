'''# Program to check vowel or consonant'''

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter a single character")
else:
    char = char.lower()

    if char in 'aeiou':
        print(char, "is a vowel")
    elif char.isalpha():
        print(char, "is a consonant")
    else:
        print("Invalid input (not an alphabet)")


'''Output 1:
Enter a character: ahaeiko
Please enter a single character

Ouput 2:
Enter a character: i
i is a vowel'''