# Inventory Management System

# Initial list of stock items
stock_items = [
    {"id": 1, "name": "Pen", "quantity": 20, "price": 10000},
    {"id": 2, "name": "Notebook", "quantity": 40, "price": 250000},
    {"id": 3, "name": "Pencil", "quantity": 40, "price": 5000}
]

# Menu loop
while True:
    print("\n=== Inventory Menu ===")
    print("1. Display Stock")
    print("2. Update Stock")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

 # Display stock
    if choice == "1":
        print("\n--- Current Stock ---")
        for item in stock_items:
            print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: shs.{item['price']}")

 # Update stock
    elif choice == "2":
        try:
            item_id = int(input("Enter item ID to update: "))
            found = False

            for item in stock_items:
                if item["id"] == item_id:
                    print(f"Current Quantity: {item['quantity']}, Price: shs.{item['price']}")
                    item["quantity"] = int(input("Enter new quantity: "))
                    item["price"] = int(input("Enter new price: "))
                    print("Item updated.")
                    found = True
                    break
            
            if not found:
                print("Item not found.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Exit program
    elif choice == "3":
        print("Exiting")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
