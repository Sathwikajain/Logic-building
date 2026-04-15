arr = [1, 2, 4, 5, 6]
n = 6 

expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)

missing = expected_sum - actual_sum

print("Missing Number:", missing)