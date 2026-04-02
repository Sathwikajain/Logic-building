# Factors of a number
n = int(input("Enter a number: "))
print("Factors of", n, "are:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        


'''output:
Enter a number: 4
Factors of 4 are: 1 2 4 '''        