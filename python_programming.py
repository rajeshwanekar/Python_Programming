# -*- coding: utf-8 -*-
"""Python programming

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QDqYQL58Kqd94Y7VarrakBk2IMlL9Oev
"""

#print text program
#print("x,y,z") or print('x,y,z')
#ex :
print("Hello, World")

#print text program
#print("x,y,z") or print('x,y,z')
#ex :
print('Hello, World')

#comments
#We use hash # to note down without executing in a program
#ex :
#declare a variable
name="Josh"
#print name
print(name)     #the name is josh so we are gonna execute the program without getting inturrupted by the comments

#we can print numbers without using quotes ("") or ('') in the brackets
#ex :
print(100)

#This is how we can do the sum by using simple english statement and putting comma and variable name next to the statement in the bracket infront of the print
num1=1.5
num2=6.3
sum=num1+num2
print('The sum of num1 and num2 is',sum)

#We can print value of the variable just by putting variable in the bracket infront of the print without quotation marks
item = 'rajesh'
print(item)

item_lol='chinese'
print(item_lol)

#Capital and small letters make difference in python. ex. item, Item
item = 'Apple'
Item = 'banana'
print(item,Item)

item_name = 'Orange'
print('Hello ' + item_name)   #I have given a space inside the Hello quotes that's why there is space between Hello Orange
#To keep space without without editing in between quotes just use (,) instead of (+)

item_name = 'Orange'
print('Hello' , item_name)     #To keep space without without editing in between quotes just use (,) instead of (+)

#String and not string types can't combine, they have to be of the same types
integer = 2021
word = 'text'
isHappy = False
funny_list = ['lol','no','ok']
string_number = '33'

print(word + str(integer))    #We can not combine string and non string values. Hence we used str() on a variable named integer because it was an integer
print(20 + int(string_number))#We can not combine string and non string values. Hence we used int() on a variable named string_number because it was an string



#Calculator
a = 10
b = 15

addition = a + b
difference = a - b
multiply = a * b
divide = a/b
power = a**b

print(addition)
print(difference)
print(multiply)
print(divide)
print(power)

#Logic
age = 40

if age > 40:
  print('You are old!')
elif age == 30:
  print('You are still young!')
else:
  print('You are getting old!')

#Booleans and Logic
#Booleans are True or False
is_Happy = False
if is_Happy:
  print('They are Happy')
else:                               #Here we are only using if and else in the Logic because we only want to keep one option, but we can use both if necessary
  print('They are not Happy')

#Booleans and Logic
#Booleans are True or False
is_Happy = True
if is_Happy:
  print('They are Happy')
else:                               #Here we are only using if and else in the Logic because we only want to keep one option, but we can use both if necessary
  print('They are not Happy')

#Loop
for i in range(4):         #Here we have mention i means index and range is 4 that means the index starts from 0 and the range is 0 to 4 and that are also the values of variable i
  print(i+2)

print(range(4))        #Here we have not mentioned i that's why the range starts from 1

name_list = ['mario','steve','jack']
for name in name_list:
  print(name)

a=['lol']
for a1 in a:
  print(a1)

#calculator
x=float(input('Enter 1st number'))#Here the input is in string and not in float or integer so it will not be able to do the maths
y=float(input('Enter 2nd number'))#Here we are using float because float gives access to decimal numbers. We can also use int and complex if needed
a=x+y
print(a)

for a in range(4):
  print('Hello world')

for a in range(3):
  print(a)

x = float(input('Enter 1st number'))
y = float(input('Enter 2nd number'))
a = x + y
print(a)

age = 30
if age == 30:
  print('yes')
else :
    print('no')

