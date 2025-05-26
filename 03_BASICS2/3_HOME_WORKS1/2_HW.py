# String Manipulation Exercise: Write a Python program that:

# Takes a sentence as input from the user.
# Prints the sentence in all uppercase and lowercase.
# Replaces all spaces with underscores.
# Removes leading and trailing whitespace.

name = input("ENTER YOUR NAME :  ")

print(name.upper())
print(name.lower())
print(name.replace(' ','_'))
print(name.strip() * 6)
