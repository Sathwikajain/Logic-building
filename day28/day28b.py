s = "hello"

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count, "Consonants:", c_count)

#Vowels: 2 Consonants: 3