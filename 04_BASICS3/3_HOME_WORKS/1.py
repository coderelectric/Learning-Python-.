'''Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
'''

# Get user input for two numbers
num1 = int(input("Enter the first number: "))   
num2 = int(input("Enter the second number: "))

if num1 > 10 and num2 > 10 :
    print ('both the numbers are greater than 10 ')

else :
   print(False)

if num1 < 5 or num2 < 5 :
 print(' atleast one of the numbers is smaller than the 5 ')

else :
   print(False)

if not num1 > num2 :
   print('the first number is not greater than the second number')

else :
   print(False)




    
    







