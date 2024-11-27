# Simple calculator program

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# Show the menu to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Ask the user for their choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the input is valid
    if choice in ('1', '2', '3', '4'):
        # Try to get the numbers from the user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Oops! That wasn't a number. Try again.")
            continue

        # Perform the operation based on the user's choice
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Can't divide by zero!")

        # Ask if the user wants to keep calculating or stop
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("That's not a valid choice. Please pick a number from 1 to 4.")
