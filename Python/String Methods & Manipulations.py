# String Methods & Manipulations in Python

# 1. Changing case
s = "Hello World"
print(s.lower())      # hello world
print(s.upper())      # HELLO WORLD
print(s.title())      # Hello World
print(s.capitalize()) # Hello world

# 2. Stripping whitespace
s2 = "   Python   "
print(s2.strip())     # 'Python'
print(s2.lstrip())    # 'Python   '
print(s2.rstrip())    # '   Python'

# 3. Finding and replacing
s3 = "banana"
print(s3.find("na"))      # 2
print(s3.replace("na", "xy")) # baxyxy

# 4. Splitting and joining
s4 = "apple,banana,cherry"
fruits = s4.split(",")
print(fruits)             # ['apple', 'banana', 'cherry']
print("-".join(fruits))   # apple-banana-cherry

# 5. Checking content
s5 = "12345"
print(s5.isdigit())       # True
print(s5.isalpha())       # False
print("abc".isalpha())    # True
print("abc123".isalnum()) # True

# 6. Slicing
s6 = "abcdef"
print(s6[1:4])            # bcd
print(s6[::-1])           # fedcba

# 7. Formatting
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.") # f-string
print("My name is {} and I am {} years old.".format(name, age))

# 8. Counting substrings
s7 = "banana"
print(s7.count("a"))      # 3

# 9. Startswith/Endswith
print(s7.startswith("ba")) # True
print(s7.endswith("na"))   # True