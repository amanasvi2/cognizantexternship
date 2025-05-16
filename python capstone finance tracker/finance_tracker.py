# Welcome message
print("Welcome to the Personal Finance Tracker!")

# Initialize the data structure to store expenses
expenses = {}

# Function to add an expense
def add_expense():
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")
        
        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")
        
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Add the expense to the dictionary
        if category not in expenses:
            expenses[category] = []
        expenses[category].append((description, amount))
        print("Expense added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\nAll Expenses:")
    for category, expense_list in expenses.items():
        print(f"Category: {category}")
        for description, amount in expense_list:
            print(f"  - {description}: ${amount:.2f}")

# Function to view summary by category
def view_summary():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\nSummary:")
    for category, expense_list in expenses.items():
        total = sum(amount for _, amount in expense_list)
        print(f"{category}: ${total:.2f}")

# Main menu logic
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()