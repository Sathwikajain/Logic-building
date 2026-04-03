# Prime numbers in a range
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
print("Prime numbers between", start, "and", end, "are:", end=" ")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

output:
Enter first number: 2
Enter second number: 8
Prime numbers between 2 and 8 are: 2 3 5 7             