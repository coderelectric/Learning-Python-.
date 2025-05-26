# 2. String Manipulation
# Strings are sequences of characters. Python provides many useful methods to manipulate strings.

# 2.1 Common String Operations:
# Concatenation: Joining two or more strings together using the + operator.

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: "John Doe"

# Repetition: Repeating a string multiple times using the * operator.

greeting = "Hello! " * 3
print(greeting)  # Output: "Hello! Hello! Hello! "

# 2.2 String Methods:
'''upper(): Converts a string to uppercase.
lower(): Converts a string to lowercase.
strip(): Removes leading and trailing spaces from a string.
replace(old, new): Replaces a substring with another string.'''

message = "  Hello, World!  "

print(message.strip())  # Output: "Hello, World!"
print(message.upper())  # Output: "HELLO, WORLD!"
print(message.replace("World", "Python"))  # Output: "Hello, Python!"

# 2.3 Accessing String Characters:
# You can access individual characters in a string using indexing. Python uses zero-based indexing, so the first character has an index of 0.

text = "Python"
print(text[0])  # Output: P
print(text[2])  # Output: t

# You can also use negative indexing to start counting from the end of the string.

print(text[-1])  # Output: n
print(text[-3])  # Output: h

# 2.4 Slicing Strings:
# You can extract a portion (substring) of a string using slicing.

text = "Python Programming"
print(text[0:6])  # Output: Python (extracts from index 0 to 5)
print(text[:6])  # Output: Python (same as above)
print(text[7:])  # Output: Programming (from index 7 to the end)
