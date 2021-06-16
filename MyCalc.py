#Program name: MyCalc
#Lab no: 1
#Description: Input two numbers then select operator
#Your name: Juan Rodriguez
#Date: 06-13-2021

title = "My Calculator"
choice = "y"
while (choice == 'y'):
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    print("Please select operation to be performed:\nadd\nsubtract\nmultiply\ndivide")
    operation = input("Your choice:  ")
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        print("You didn't enter a valid operator")
    print(title)
    print("\n")
    print("The "+str(operation)+" of "+str(num1)+" and "+str(num2)+" is "+str(result)+", where "+str(operation)+" is the operation entered, "+str(num1)+" and "+str(num2)+" are the numbers entered and "+str(result)+" is the result of the operation")
    print("Press 'y' to perform other calculation \n Press 'n' to stop")
    choice = input("Your choice:  ")
print("Thanks for using the calculator")