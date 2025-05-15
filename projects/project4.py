print("Welcome to the Inventory Manager!")

# Step 1: Create the inventory
inventory = {}

# Function to display the inventory
def display_inventory():
    if not inventory:
        print("The inventory is empty.")
    else:
        print("\nCurrent inventory:")
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")

# Function to calculate total value of the inventory
def calculate_total_value():
    total_value = sum(quantity * price for quantity, price in inventory.values())
    print(f"\nTotal value of inventory: ${total_value:.2f}")

# Step 2: Add, Remove, and Update Items
while True:
    print("\nOptions:")
    print("1. Add a new item")
    print("2. Remove an item")
    print("3. Update an item")
    print("4. Display inventory")
    print("5. Calculate total value")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        # Add a new item
        item = input("Enter the item name: ").lower()
        if item in inventory:
            print(f"{item} already exists in the inventory.")
        else:
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price: "))
            inventory[item] = (quantity, price)
            print(f"{item} has been added to the inventory.")
    
    elif choice == "2":
        # Remove an item
        item = input("Enter the item name to remove: ").lower()
        if item in inventory:
            del inventory[item]
            print(f"{item} has been removed from the inventory.")
        else:
            print(f"{item} does not exist in the inventory.")
    
    elif choice == "3":
        # Update an item
        item = input("Enter the item name to update: ").lower()
        if item in inventory:
            quantity = int(input("Enter the new quantity: "))
            price = float(input("Enter the new price: "))
            inventory[item] = (quantity, price)
            print(f"{item} has been updated in the inventory.")
        else:
            print(f"{item} does not exist in the inventory.")
    
    elif choice == "4":
        # Display the inventory
        display_inventory()
    
    elif choice == "5":
        # Calculate total value
        calculate_total_value()
    
    elif choice == "6":
        # Exit the program
        print("Exiting the Inventory Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")