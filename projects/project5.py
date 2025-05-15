import turtle

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive function to draw a fractal tree (bonus)
def draw_fractal_tree(t, branch_length):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(t, branch_length - 15)
        t.left(40)
        draw_fractal_tree(t, branch_length - 15)
        t.right(20)
        t.backward(branch_length)

# Menu-driven program
def main():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        
        choice = input("> ")
        
        if choice == "1":
            # Factorial calculation
            try:
                num = int(input("Enter a positive integer to find its factorial: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The factorial of {num} is {factorial(num)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        elif choice == "2":
            # Fibonacci calculation
            try:
                num = int(input("Enter the position of the Fibonacci number: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        elif choice == "3":
            # Draw fractal pattern
            print("Drawing a fractal tree... Close the window to return to the menu.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.speed(0)
            t.left(90)
            t.up()
            t.backward(100)
            t.down()
            draw_fractal_tree(t, 100)
            screen.mainloop()
        
        elif choice == "4":
            # Exit the program
            print("Thank you for using the Recursive Artistry Program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()