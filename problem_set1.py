# Physics IDC Python course (Modern computational)

# Name: Arpan Purkait
# Roll: 002320701045
import math as m

# Problem sets-1
'''
Application of “print, numbers, input”
1. Write a program that takes two numbers (int, float,) as input
from the user and prints their
sum, difference, product, and quotient.
2. Write a program that takes the length and width of a rectangle
from the user and prints its
area and perimeter.
3. Take two numbers as input and swap them without using a third
variable.
4. Take the principal amount, rate of interest, and time period
from the user, then calculate
and print the simple interest.
5. Take a temperature in Celsius from the user and convert it to
Fahrenheit.
input(), if-else conditions, print(), modulus %
6. Write a program that takes three numbers as input and prints
the largest one
7. Take a number as input and print whether it is even or odd.
8. Take a three-digit number as input and print the sum of its
digits
“for” loop
9. Take a number as input and print its factorial.
10. Take a number as input and print its multiplication table up
to 10.
'''

# Codes/Answers

'''
Q - 1: Write a program that takes two numbers (int, float,) as input
from the user and prints their sum, difference, product, and
quotient.
'''
number_1 = float(input("Entre first Number:"))
number_2 = float(input("Entre second Number:"))

sums = number_1 + number_2
diff = abs(number_2 - number_1)
product = number_1 * number_2

try:
  quoti = number_1/number_2
except ZeroDivisionError:
  quoti = m.inf
  
print(number_1)
print(number_2)
print(sums)
print(diff)
print(product)
print(quoti)




'''
Q-3: Write a program that takes the length and width of a rectangle
from the user and prints its area and perimeter.
'''

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")



'''
Q-3: Take two numbers as input and swap them without using a third
variable.
'''
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")




'''
Q-4: Take the principal amount, rate of interest, and time period
from the user, then calculate and print the simple interest.
'''
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: {simple_interest}")





'''
Q-5: Take a temperature in Celsius from the user and convert it to
Fahrenheit.
'''
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")




'''
Q-6: Write a program that takes three numbers as input and prints
the largest one
'''

user_input = input("Entre numbers by space: ")
numbers = list(map(int,user_input.split()))        ###################

k = 0
for i in range (len(numbers)):
  if (numbers[k] < numbers[i]): k = i
print("Largest Number: ", numbers[k])





'''
Q-7: Take a number as input and print whether it is even or odd.
'''

num = int(input("Enter a number: "))
print("Even.") if num % 2 == 0 else print("Odd.")




'''
Q-8: Take a three-digit number as input and print the sum of its
digits
'''

# // - stands for integer division
num = int(input("Enter a three-digit number: "))

digit1 = num // 100
digit2 = (num // 10) % 10                 ##########################
digit3 = num % 10

sum_digits = digit1 + digit2 + digit3
print(f"Sum of the digits: {sum_digits}")






'''
Q-9: Take a number as input and print its factorial.
'''
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
factorial *= i
print(f"Factorial of {num} is: {factorial}")





'''
Q-10: Take a number as input and print its multiplication table up
to 10.
'''
num = int(input("Entre a number:"))
for i in range(1,11):
print(f"{num} x {i} = {num * i}")





