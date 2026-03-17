# Demonstration of all operators in Python

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Assignment Operators
print("\nAssignment Operators:")
c = a
print("Assign:", c)
c += b
print("Add and assign:", c)
c -= b
print("Subtract and assign:", c)
c *= b
print("Multiply and assign:", c)
c /= b
print("Divide and assign:", c)
c //= b
print("Floor divide and assign:", c)
c %= b
print("Modulus and assign:", c)
c **= b
print("Exponentiate and assign:", c)

# Comparison Operators
print("\nComparison Operators:")
print("Equal:", a == b)
print("Not equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater or equal:", a >= b)
print("Less or equal:", a <= b)

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("and:", x and y)
print("or:", x or y)
print("not:", not x)

# Bitwise Operators
print("\nBitwise Operators:")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# Membership Operators
print("\nMembership Operators:")
lst = [1, 2, 3, 10]
print("in:", a in lst)
print("not in:", b not in lst)

# Identity Operators
print("\nIdentity Operators:")
m = a
n = b
print("is:", m is a)
print("is not:", n is not a)