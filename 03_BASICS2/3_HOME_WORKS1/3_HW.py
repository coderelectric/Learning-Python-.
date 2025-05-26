# Character Counter: Write a Python program that:

# Asks the user for a string.
# Prints how many characters are in the string, excluding spaces.

name = input("ENTER YOUR NAME :  ")

# Count characters excluding spaces

print(f"number of alphabets in your name is : {len(name.replace(' ', ''))}")