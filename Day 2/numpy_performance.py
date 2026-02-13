import time
import numpy as np

# Create large dataset
size = 1_000_000
numbers = list(range(size))

# Python loop
start = time.time()
total = 0
for n in numbers:
    total += n
end = time.time()

print("Loop Time:", end - start)


# NumPy vectorized
array = np.array(numbers)

start = time.time()
total_np = np.sum(array)
end = time.time()

print("NumPy Time:", end - start)

squared = []
for n in numbers:
    squared.append(n * n)

squared_np = array * array
print(squared_np)

