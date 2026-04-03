# Factorial series
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
    print(i, "! =", fact)

ouput:
Enter a number: 4
1 ! = 1
2 ! = 2
3 ! = 6
4 ! = 24    