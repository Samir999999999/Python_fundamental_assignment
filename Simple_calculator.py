# Code by Samir chaudhary

def add(x, y):
    """Function for addition"""
    return x + y

def subtract(x, y):
    """Function for subtraction"""
    return x - y

def multiply(x, y):
    """Function for multiplication"""
    return x * y

def divide(x, y):
    """Function for division"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    print("===================")

    # Ask the user to select an operation
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))

        if choice in [1, 2, 3, 4]:
            # Get user input for numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation
            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    calculator()