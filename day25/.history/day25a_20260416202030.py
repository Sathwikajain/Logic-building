arr = [1, 2, 2, 3, 1, 4, 5, 1]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)