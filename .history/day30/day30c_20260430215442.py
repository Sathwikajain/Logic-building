data = {"name": "John", "age": 25, "city": "New York"}

swapped = {value: key for key, value in data.items()}

print(swapped)