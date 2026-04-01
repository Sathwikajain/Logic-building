# Convert number to words

num = input("Enter a number: ")
words = ["Zero", "One", "Two", "Three", "Four",
         "Five", "Six", "Seven", "Eight", "Nine"]
print("Output:", end=" ")
for digit in num:
    print(words[int(digit)], end=" ")
    


    