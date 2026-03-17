# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Dictionary key/value handling
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])

# Adding a new key/value
my_dict['email'] = 'alice@example.com'

# Updating a value
my_dict['age'] = 31

# Iterating over keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if 'city' in my_dict:
    print("City exists:", my_dict['city'])

# Removing a key/value
del my_dict['email']
print("After deletion:", my_dict)