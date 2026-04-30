s = "programming"

freq = {}
duplicates = []

# Count frequency
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Collect duplicates
for ch in freq:
    if freq[ch] > 1:
        duplicates.append(ch)

print("Duplicate characters:", duplicates)


#output:Duplicate characters: ['r', 'g', 'm']