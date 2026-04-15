arr = [1, 1, 0, 1, 1, 1]
max_count = 0
count = 0
for num in arr:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print("Longest consecutive 1s:", max_count)

#output:
#Longest consecutive 1s: 3