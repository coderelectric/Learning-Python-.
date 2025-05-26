'''
simple greeting program: write a python program that asks user for name and age  then writes a personalised greeting message .
use both the + operator and f strings for output
                                                      '''
name = input(" ENTER YOUR NAME :  ")
age = input(" ENTER YOUR AGE :  ")

print('Hi! ' + name + ' you are ' + str(age) + " year old "  )

print(f'hi! {name} you are {age} year old')

