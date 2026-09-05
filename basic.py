#Hello word
print ("Hello word")
#comment
#1 Line comment
#print("Hello word")
#2 or more line comment
"""
This is a multi-line comment.
It can have two or more lines.
Python will treat it as a string.
"""
#Variable
name = "Jalal Khan"
Age = 22
time = "2 O clock"
Date = "5/9/2026"
print(name)
print(Age)
print(time)
print(Date)

#Data Type
#String
intro="My name is Abdul Jalal Khan ..."
print(intro)
#integer
Age = 22
print(Age)
#Float
Height = 5.6
print(Height)
#Boolean 
x=20
print(x>6)
print(x<6)
print(x>30)
#2
password = "jalal 1122"
correct_password = password == "jalal 1122"
print(correct_password)

#Operators
  # Addition
a = 3
b = 4 
print (a+b)
# Subtraction
print(a - b)
# Multiplication
print(a * b)  
# Division
print(a / b)  
# Floor division 
print(a // b) 
# Remainder
print(a % b)   
 # Power
print(a ** b) 

"""Comparison Operators
These compare two values."""
print(a == b)
print(a != b)
print(a >= b) 
#Logical Operators "AND"
age = 25
print (age >18 and age<30)
print (age <10 and age>8)
#OR Operator
age = 19
print (age >20 or age <20)
#Conditional Statements "if...else"
age = 20

if age >= 18:
    print("You are an adult")
else :
 print("you are not adult")
#if...elif...else
marks = 35
if marks >= 80:
 print("A")
elif marks >=70:
 print ("B")
elif marks >=50:
  print("E")
else :
  print("Fail")
#Dictionary 
#Access, update, and delete entries
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}
print ( student["name"])
print (student["age"])
student ["age"] =21
#Loops (For)
for i in range (7):
  print (i)
#2
fruit = ["Bnana , Mnago, apple"]
Brand = ["BMW", "Audi", "Corolla", "Nissan"]

for i in Brand:
    print(i)

#Range
for i in range (5):
  print (i)
#break
for i in range (1,50):
 if i == 9 :
  break
print (i)
#continue
for i in range(20,25) :
  if i == 22:
   continue
  print(i)
#pass
for i in range (5):
  pass
#Functions
#Defining a Function
def greet(name):
    print("Hello", name)

greet("Ali")
greet("Ahmed")
#Multiple parameters
def add (a,b):
  print (a+b)
add(10,20)
#Lambda Functions
# Lambda with map()
numbers = [1, 2, 3, 4, 5]
result= list(map(lambda x: x*2, numbers))
print(result)
#Lambda with filter()
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
#List Comprehension
number = [i for i in range(1,6)]
print(number)
#Even numbers
list_even = [i for i in range(1, 10) if i % 2 == 0]
print(even_numbers)