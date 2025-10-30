def takeInput():
    while True:
        user_input = input("Enter a number: ")
        try:
            num = float(user_input)
            return num 
        except ValueError:
            print("You can only enter a number.")

def takeSign():
    while True:
        user_input = input("Enter an operation sign ('+','-', '*', '/'):")
        if user_input in ("+", "-", "*", "/"):
            sign = user_input
            return sign
        else:
            print("You can only enter '+', '-', '*' or '/'")

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "\"Just divide it by zero\" - brutal"

print("Enter two numbers")
num1 = takeInput()
num2 = takeInput()

sign = takeSign()

if sign == "+":
    print(f"{num1} + {num2} = {addition(num1, num2)}")
elif sign == "-":
    print(f"{num1} - {num2} = {substraction(num1, num2)}")
elif sign == "*":
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
elif sign == "/":
    print(f"{num1} / {num2} = {division(num1, num2)}")