#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 15:53:44 2025

@author: arpan
"""
'''
mylist = ["Arpan","Don","Jon", 1,0.11,False,"Ayan","Modi",3]

for i in range (len(mylist)):
    print(mylist[i])
    
print(mylist[:])
print(mylist[:3])
print(mylist[3:])
print(mylist[2:3])

name = "   Indian Institute of Technology    "

stripedname = name.strip(" ")
print(name)
print(stripedname)


position = stripedname.find("Tec")
print(position)

count = name.count("T")
print(count)

def fact(n):
    if(n<0):
        print("NO FACTORIAL FOR -VE NUMBER")
    elif(n==0):
        return 1
    else:
        f = 1
        for i in range (1,n+1):
            f = f * i
        return f
'''
'''
for i in range (1, 1000):    
    for j in range (1, fact(i)):
        i = i * i
        print(i)
    print("\n") '''
'''
def isPrime(n):
    for i in range(2,n):
        if (n%i == 0):
            return False
        else: 
            return True


i = 0
while i < 5:
    print(i)
    i = i + 1
'''


'''
    
for n in range (1, 10000000000):    
    temp = n
    l = len(str(n))
    sums = 0
    while(temp>0):
        temp2 = temp%10
        sums = sums + pow(temp2,l)
        temp = temp //10
    if (sums == n):
        print(n)
        
        
isEVEN = lambda x: "Even" if (x%2 == 0) else "Odd"
'''

myList = ["a","b","c","d","e"]
print(myList[::-1])  
myList.reverse()
print(myList)
myList.append("f")
print(myList)
myList.pop(1)
print(myList)
myList.remove("f")
print(myList)

myTuple = (1,2,3,4,5,6)
myTuple = list(myTuple)
# Make changes
myTuple = tuple(myTuple) 


# list, tuple, dictionary, sets


import math as m

print(m.pi,m.acos(-1.0))


class name:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
if __name__ == "__main__":
    p1 = name("Arpan","Purkait")
    print(p1.lastname)
