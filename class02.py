
# author: Kanan

#-----------------------Working with strings-------------------------

'''
Character_name="Gopal" #String type
e="5" #String type
print("There is a boy \n named", Character_name) #next line \n
print(Character_name, "is a very good boy")
print(Character_name, "is 25 years old")
print(Character_name.lower())
print(Character_name.upper())
print(Character_name.isupper())
print(len(Character_name))
print(Character_name[0])
print(Character_name.index("p"))
print(Character_name.index("al"))
print(Character_name.replace("Go", "Arka"))

statement_type1=True #Booean variable

name = "gukesh"
print(name.title())
'''
#-----------------Building a basic calculator------------------------------
'''
number1 = input("Enter a number:") #it assumes the input as 'string'
number2 = input("Enter another number: ")
#sum = int(number1) + int(number2) #integer numbers should be entered
sum_float = float(number1)+float(number2)
#print(sum)
print(sum_float)
'''
#---------------------------------Lists-------------------------------------
'''
mylist = ["Babu", 2, True, "Apple", "Footbal", "Pen"]
print(mylist)
print(mylist[3])
print(mylist[-2])
print(mylist[1:])
print(mylist[:2]) #print first 2 elements
print(mylist[2:4])
mylist[1]=5
print(mylist)

'''
#---------------------------Lists of functions------------------------------
'''
mylist1 = ["Babu", "Apple", "Footbal", "Pen", "Notes"]
numbers = [2,7,9,4,10,43, 67]
print(mylist1)
mylist1.extend(numbers)
print(mylist1)
numbers.append(7)
print(numbers)
numbers.insert(2, 200)
print(numbers)
numbers.remove(200)
print(numbers)
numbers.clear()
print(numbers)
print(mylist1.index("Footbal"))
#mylist1.sort()
numbers = [2,7,9, 67,4,10,43]
numbers.sort()
print(mylist1)
print(numbers)
numbers.reverse()
print(numbers)

numbers2=numbers.copy()
print(numbers2)
'''

