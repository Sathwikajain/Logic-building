s = "abc123!@#"

result = ""

for ch in s:
    if ch.isalpha():
        result += ch

print("Output:", result)

