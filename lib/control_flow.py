#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    #  If the username is "admin" or "ADMIN" and the password is "12345"or
    if username.lower()=='admin' and password == 1234:
        print('Access granted')
    else:
        print('Access denied')
admin_login("admin",12434)
def hows_the_weather(temperature):
    # your code here
   if temperature<40:
       print("It's brisk out there!")
   elif temperature >40 and temperature < 65:
       print("It's a little chilly out there!")
   elif temperature >85:
       print("It's too dang hot out there!")
   else:
       print("It's perfect out there!")
hows_the_weather(6)

def fizzbuzz(num):
    # your code here
    if num % 3==0 and num % 5 ==0:
        print('FizzBuzz')
    elif num % 3==0:
        print('Fizz')
    elif num % 5==0:
        print('Buzz')
    else:
        print(num)
fizzbuzz(15)

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    else:
        print('Invalid operation')
calculator('+', 4, 2)

