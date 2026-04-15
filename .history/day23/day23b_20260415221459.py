arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]

candidate = None
count = 0

# Step 1: Find candidate
for num in arr:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)

# Step 2: Verify
if arr.count(candidate) > len(arr) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element")