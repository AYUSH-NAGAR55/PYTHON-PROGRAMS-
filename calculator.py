# write a python program to make a simple calculator.

def calculator():    # defines a function for the calculator
    while True:      # create an infinite loop to keep the calculator running
        # prints the menu option
        print("\n1. Addition")         
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        choice = input("Choose an option: ")     # ask the user to choose and 
        if choice in ["1","2","3","4"]:          # check if the user choose the valid option
            num1 = float(input("Enter first number: "))    # ask the user to enter numbers
            num2 = float(input("Enter second number: "))
            # perform the chosen option
            if choice == "1":
                print(f"{num1} + {num2} = {num1 + num2}")   # ADDITION
            elif choice == "2":
                print(f"{num1} - {num2} = {num1 - num2}")   # SUBTRACTION
            elif choice == "3":
                print(f"{num1} * {num2} = {num1 * num2}")   # MULTIPLICATION
            elif choice == "4":
                if num2 != 0:
                   print(f"{num1} / {num2} = {num1 / num2}")# DIVISION
            else: 
                print("Error: Division by zero is not allowed." )   # handle division by zero
        elif choice == "5":
            break                   # quit the calculator
        else:
            print("Invalid option.")
            
calculator()    # call the calculator function