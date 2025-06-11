"""
@author: Kanan
"""

'''
print("Hello world")
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

#Variables in Python
a=2 #variable type numbers
b=3.5 #3
c=a+b
print(c)#"c# string type
'''

import math as m
#-----------------------Working with numbers---------------------------
mynum=-10
print(0) #-20, 20.38445
print(str(mynum) , "is my favourite number")
print(abs(mynum))
print(pow(mynum, 2.))
# pow(2**3)
print(max(1,2,3.3, -23, 4,5))
print(min(1,2,3.3, -23, 4,5))
print(round(3.2))
print(round(3.6))
print(m.floor(30.6))
print(m.ceil(30.6))
print(m.sqrt(32.))

#------------------------Getting inputs from user--------------------------

name = input("Enter your name:")
age = input("Enter your age: ")
print("Hello", name, "!", "You are", age, "years old !")

