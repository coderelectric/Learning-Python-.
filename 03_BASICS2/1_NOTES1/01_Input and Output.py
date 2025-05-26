## **Input/Output,

### **1. Input and Output in Python**

#### **1.1 Input from the User:**
'''In Python, we use the `input()` function to take input from the user. The data entered by the user is always received as a string, so if you want to use it as a different data type (e.g., integer or float), you'll need to convert it using type conversion functions like `int()` or `float()`.

```python '''

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer


#### **1.2 Output to the Console:**
'''The `print()` function is used to display output to the console. You can use it to display text, variables, or results of expressions.

```python'''

print("Hello, " + name + "! You are " + str(age) + " years old.") # Output: Hello, Alice! You are 25 years old.
'''
You can also use **f-strings** (formatted string literals) for more readable code:
```python
             '''

print(f"Hello, {name}! You are {age} years old.")    # Output: Hello, Alice! You are 25 years old.
