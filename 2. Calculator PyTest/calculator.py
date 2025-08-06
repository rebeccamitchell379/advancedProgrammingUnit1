# Define function to add two numbers
def add(x, y):
    return x + y

# Define function to subtract two numbers
def subtract(x, y):
    return x - y

# Define function to multiply two numbers
def multiply(x, y):
    return x * y

# Define function to divide two numbers
def divide(x, y):
    # Check if the divisor is zero
    if y == 0:
        # Raise a ValueError if dividing by zero
        raise ValueError("Cannot divide by zero")
    return x / y

# Main function to execute the calculator
def main():
    # Print the menu for selecting operation
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Prompt user to enter choice
    choice = input("Enter choice (1/2/3/4): ")

    # Prompt user to enter two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the operation based on user's choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        try:
            print("Result:", divide(num1, num2))
        except ValueError as e:
            print(e)  # Handle division by zero exception
    else:
        print("Invalid input")  # Handle invalid choice

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
