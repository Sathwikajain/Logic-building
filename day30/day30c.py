data = {"name": "John", "age": 25, "city": "New York"}

swapped = {value: key for key, value in data.items()}

print(swapped)

#output:{'John': 'name', 25: 'age', 'New York': 'city'}