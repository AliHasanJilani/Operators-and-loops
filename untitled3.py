# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oHUreBajTj0MAaBn9Gt3qW5FNpSWyiC3
"""

#Q13 Write a program that simulates a simple ATM. The user should be able to:
#Check balance
#Deposit money
#Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices.

city="RAJASTHAN"
print( city[0:9])

city="RAJASTHAN"
print( city[-9:])

city="RAJASTHAN"
print( city[2:7:3])

city="RAJASTHAN"
print( city[0:4:-1])

city="RAJASTHAN"
print( city[-1:-3])

city="RAJASTHAN"
print( city[::-1])

city="RAJASTHAN"
print( city[:])

# Arithmetic
# + - * / // % , **

# normal division
10/2 # it give the answer in interger

#floor division
10//2  # it give the answer in interger

# assignment operators
x=10
x=x+15    # x+=5
print(x)

y=6
y/=3  #y=y/3
print(y)

# += , **= , %=

#logical opearator
# and or not

# membership operator
"z" in "yash"

# These operator are (in , not)
9 in [10,20,30,9,4]

# identity operator
# (is , is not)---> identity operator
# to check whether a variable is a instance of class or not
# to check the memory addresss
x=10
type(x) is int

# bitwise operator
# 0,1
# & --> and operator
# 8421

11 & 18
13 & 7

# right shift formula ---> number // 2**bit
# 54 >> 3
#54 // 2**3
# 54 // 8 --> 6

54>>3

# leftshift formula ---> number * 2**bit

# loops
# for loop
for i in range(0,10):
  print(i)

for i in range(0,10,2):
  print(i)

for i in range(50,9,-1):
  print(i)

total=0
for i in range(1,11):
  total=total+i
  print(total)

count=0
for i in range(69,3,-1):
 count=count+1
print(count)

for i in range(13,0,-1):
  if(i%3==0):
    print(i)

for i in range (55,22,-1):
  if(i%2==0):
    print(i)
  else:
    print()

# 1. What is the D/f call by value and call by reference
# 2. What is ask value and utm value
# 3. Different data type in python
# 4. D/f is operator and equal equal to operator
# 5. what is opps concepts
