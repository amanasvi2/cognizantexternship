# Task 1 - Understanding Python Exceptions
def divide_by_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            result = 100 / num
            print(f"100 divided by {num} is {result}.")
            break
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Example usage
divide_by_number()

# Task 2 - Types of Exceptions
def handle_exceptions():
    # IndexError example
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Accessing an invalid index
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # KeyError example
    try:
        my_dict = {"name": "Archita"}
        print(my_dict["age"])  # Accessing a non-existent key
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # TypeError example
    try:
        result = "string" + 5  # Adding a string and an integer
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

# Example usage
handle_exceptions()

# Task 3 - Using try...except...else...finally
def divide_with_finally():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

# Example usage
divide_with_finally()