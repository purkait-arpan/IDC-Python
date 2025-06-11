# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 07:23:03 2021

@author: Kanan
"""

  

#-----------------------While loop--------------          
 
i=0
while i<=10:
    print(i)
    i=i+1 #or i+=1


#----------------------"for loop"----------------
    
for i in range(10+1):
    print(i)   


print("\n")  
  
for i in range(3,10):
    print(i) 
   
list1=[2,4.2, 3.4, 3.,5., 9.2, 21.]

for i in range(len(list1)):
    print(list1[i])  
    
list2 = ["Rama", "Sama", "Jadu", "Madhu"] 
for i in range(len(list2)):  
    print(list2[i])
