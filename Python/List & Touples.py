# Demonstrating Lists and Tuples in Python

# List operations
my_list = [1, 2, 3, 4]
print("Original list:", my_list)

# Append
my_list.append(5)
print("After append:", my_list)

# Insert
my_list.insert(2, 10)
print("After insert:", my_list)

# Remove
my_list.remove(2)
print("After remove:", my_list)

# Pop
popped = my_list.pop()
print("After pop:", my_list, "| Popped element:", popped)

# Index
index_of_10 = my_list.index(10)
print("Index of 10:", index_of_10)

# Sort
my_list.sort()
print("Sorted list:", my_list)

# Reverse
my_list.reverse()
print("Reversed list:", my_list)

# Tuple operations
my_tuple = (1, 2, 3, 4)
print("\nOriginal tuple:", my_tuple)

# Count
count_2 = my_tuple.count(2)
print("Count of 2:", count_2)

# Index
index_of_3 = my_tuple.index(3)
print("Index of 3:", index_of_3)

# Tuples are immutable, so no append, remove, or sort operations
# Attempting to modify a tuple will raise an error
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Tuple modification error:", e)