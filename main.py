def takeInput():
    while True:
        user_input = input("Enter a number: ")
        try:
            num = int(user_input)
            return num 
        except ValueError:
            print("You can only enter a number.")

print("Enter two numbers:")
num1 = takeInput()
num2 = takeInput()
