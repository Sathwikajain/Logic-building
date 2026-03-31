# Fibonacci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

Output:
Enter the number of terms: 4
Fibonacci series: 0 1 1 2 
