import logging

# Configure logging to log errors to a file
logging.basicConfig(filename="error_log.txt", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def get_number(prompt):
    """Prompt the user to enter a number and validate the input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    """Main calculator program."""
    print("Welcome to the Error-Free Calculator!")
    
    while True:
        # Display menu
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("> ")
        
        if choice == "1":
            # Addition
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"The result of addition is: {num1 + num2}")
        
        elif choice == "2":
            # Subtraction
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"The result of subtraction is: {num1 - num2}")
        
        elif choice == "3":
            # Multiplication
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"The result of multiplication is: {num1 * num2}")
        
        elif choice == "4":
            # Division
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            try:
                result = num1 / num2
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
                logging.error(f"ZeroDivisionError occurred: {e}")
            else:
                print(f"The result of division is: {result}")
        
        elif choice == "5":
            # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()