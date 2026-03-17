import numpy as np

py_list=[1,2,3,4]

np_array=np.array([1,2,3,4])

print(type(py_list))
print(type(np_array))

print(np_array * 2)
print(np_array + 5)
print(np_array ** 2)

X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(X.shape)

W = np.array([
    [0.5],
    [1.0]
])

b = 2

Y = X @ W + b

print(Y)

A = np.array([1, 2, 3])
B = np.array([10])

print(A + B)


import time

size = 5_000_000
arr = np.random.rand(size)

start = time.time()
result = arr * 5
end = time.time()

print("Vectorized multiply time:", end - start)

#bias effect
import numpy as np

X = np.array([[1, 2]])
W = np.array([[1], [1]])

# Without bias
print(X @ W)

# With bias
b = np.array([[5]])
print(X @ W + b)


