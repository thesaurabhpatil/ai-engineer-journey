# Demonstration of functions in Python

# 1. Simple function without parameters
def greet():
    print("Hello, welcome to Python functions!")

# 2. Function with parameters
def add(a, b):
    return a + b

# 3. Function with default parameter
def multiply(a, b=2):
    return a * b

# 4. Function returning multiple values
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# 5. Function with variable number of arguments
def print_all(*args):
    for arg in args:
        print(arg)

# Calling the functions
greet()
print("Sum:", add(5, 3))
print("Product:", multiply(4))
print("Product with custom multiplier:", multiply(4, 5))
q, r = divide_and_remainder(10, 3)
print("Quotient:", q, "Remainder:", r)
print_all("apple", "banana", "cherry")