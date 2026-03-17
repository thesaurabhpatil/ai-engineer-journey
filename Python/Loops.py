# Demonstrating loops in Python

# 1. For loop
print("For loop:")
for i in range(5):
    print(i)

# 2. While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# 3. Looping through a list
print("\nLooping through a list:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 4. Nested loops
print("\nNested loops:")
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")