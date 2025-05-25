# TO FIND THE LEAP YEAR

a = int(input("ENTER THE YEAR :  "))

""" 
leap year rules 
if a year is divisible by 4 then it might be a leap year
but if divisible by 100 then not a leap year
unless also divisible by 400"""

t = a % 4
v = a % 100
s = a % 400

if (t == 0 and  v != 0) or (s== 0 ):

   print (a , " is   a leap year")

else :
   print(a , "is not a leap year")