num = int(input("Enter number: "))
largest = 1
for i in range(2, num + 1):
    if num % i == 0
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break       
        if is_prime:
            largest = i
print("Largest Prime Factor:", largest)