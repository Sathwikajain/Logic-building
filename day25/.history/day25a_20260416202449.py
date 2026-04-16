arr = [1, 2, 2, 3, 1, 4, 5, 1]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)

#output:
{1: 3, 2: 2, 3: 1, 4: 1, 5: 1}