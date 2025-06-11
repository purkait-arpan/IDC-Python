# IDC-3: Modern Computational Methods (Python)

# Arpan Purkait
# Roll: 002320701045
# Problem sets-2
# Codes/Answers







# Q-1: Calculate BMI and print whether underweight, normal weight, overweight, obese:
mass = float(input("Entre your mass (in Kg):"))
height = float(input("Enter your height (in Meter):"))
bodyMassIndex = mass/(height**2)
print(f"Your BMI is {bodyMassIndex:.2f}")

if bodyMassIndex < 18.50:
    category = "Under Weight"
elif 18.50 <= bodyMassIndex < 24.90:
    category = "Normal Weight"
elif 24.90 <= bodyMassIndex < 30.00:
    category = "Over Weight"
elif bodyMassIndex > 30.00:
    category = "Obesity"

print(f"You are under {category}.")






# Q-2: Paper, rock, scissor game with computer.
import random

def get_computer_choice():
    choice = ["rock", "paper", "scissors"]
    return random.choice(choice)

def winner(user,computer):
    if user == computer:
        return "It is a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer Win!"

def play():
    print("-"*30)
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thank You!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choice again.")
            user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thank You!")
            break
            
        computer_choice = get_computer_choice()
        print(f"Computer choice: {computer_choice}")

        result = winner(user_choice,computer_choice)
        print(result)
        print("-"*30)

# Uncomment the line below to play the game
play()







# Q-3: Write a Python program that asks the user to input a number and then checks if the number is even or odd.
number = int(input("Enter a integer number:"))
res = "Even" if number%2 == 0 else "Odd"
print(f"The number is: {res}")







# Q-4: Write a Python program that checks if a given year is a leap year. A year is a leap year if: Hints: It is divisible by 4, except for years that are divisible by 100 but not divisible by 400.
year = int(input("Enter Year = "))
if year %4 == 0:
    if year %100 == 0:
        res = "Leap Year" if year %400 == 0 else "Normal year"
    else:
        res = "Leap Year"
else:
    res = "Normal Year"
print(f"The Year is {res}")








# Q-5: Write a program that asks the user to input two numbers and a mathematical operation (+, -, *, /). The program then performs the operation and outputs the result. If the user enters an invalid operation, print an error message.
#x, y, operation = input("Enter input-1, input-2 and operation (between + -*/):").split()
#print(eval(f"{x}{operation}{y}") if operation in "+-*/" else "Invalid operation")







# Q-6: Take a number as input and print its factorial using both for and while loops.
n = int(input())

#..... Using for loop .....
f = 1
for i in range(2, n+1): f *= i
print(f)

# .....Using while loop.....
f, i = 1, 2
while i <= n: f *= i; i += 1
print(f)








# Q-7: Write a Python program that checks if a number n is prime or not. Use the “for” loop.
def isPrime(x):
  for i in range(2,x):
    if x%x == 0:
      return False
  return True

n = int(input("Enter Number ="))
print("Prime" if n>1 and isPrime(n) else "Not Prime")







# Q-8: Write a program that prints the first n numbers of the Fibonacci sequence using a for loop.
n = int(input("Enter Number:"))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b








# Q-9: Bisection Method for Root Finding: Find the root of a function using the bisection method. Use a while loop to iterate until the root is found within a given tolerance.
def bisection(f,a,b):
    while True:
        c = 0.5*(a+b)
        if abs(f(c)) <= 0.0001:
            return c
        else:
            a, b = (c, b) if f(c) < 0 else (a, c)

f_bisection = lambda x: (x**2 - 2)
print(f"The root is {bisection(f_bisection, 0, 5)}")








# Q-10: Newton’s Method for Solving Equations: Implement Newton-Raphson method to find roots of a given function. Use a while loop to update the estimate until convergence.
def Newton(f,df,a):
    while True:
        if abs(f(a)) <= 0.0001:
            return a
        else:
            a = a-(f(a)/df(a))

f_newton = lambda x: (x-4)**2
df_newton = lambda x: 2*(x-4)
print(f"The root is {Newton(f_newton,df_newton,10)}")








# Q-11: Take a number as input and print its multiplication table up to 10.
number = int(input("Enter number:"))
print(*[f"{number} x {i} = {number * i}" for i in range (1,11)], sep="\n")







# list comprehension Method
