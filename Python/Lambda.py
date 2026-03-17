from functools import reduce

# Lambda function example
add = lambda x, y: x + y
print("Lambda add:", add(2, 3))

# Map example: square each number
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Map squared:", squared)

# Filter example: keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filter evens:", evens)

# Reduce example: sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Reduce sum:", total)