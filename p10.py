# In-Memory Inventory Tracker with Dictionary Merging
# Inventories of three stores
store1 = {"Rice": 50, "Wheat": 30, "Sugar": 20}
store2 = {"Rice": 40, "Sugar": 25, "Oil": 15}
store3 = {"Wheat": 20, "Oil": 10, "Salt": 35}

# Function to display inventory
def display(inventory):
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} units")

# Function to check and access stock
def check_stock(inventory, item):
    if item in inventory:
        print(f"{item} exists: {inventory[item]} units")
    else:
        print(f"{item} not found. Stock: {inventory.get(item, 0)}")

# Merge inventories using dictionary comprehension
def merge_inventory(*stores):
    items = set().union(*(store.keys() for store in stores))
    return {
        item: sum(store.get(item, 0) for store in stores)
        for item in items
    }

# Main program
while True:
    print("\n1. Display Store 1")
    print("2. Display Store 2")
    print("3. Display Store 3")
    print("4. Check stock")
    print("5. Merge inventories")
    print("6. Add stock")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice in ("1", "2", "3"):
        display([store1, store2, store3][int(choice) - 1])
    elif choice == "4":
        store = input("Enter store (1/2/3): ")
        item = input("Enter item: ").title()
        inventory = {"1": store1, "2": store2, "3": store3}.get(store)

        if inventory is not None:
            check_stock(inventory, item)
        else:
            print("Invalid store!")

    elif choice == "5":
        merged = merge_inventory(store1, store2, store3)
        print("Combined Inventory:")
        display(merged)

    elif choice == "6":
        store = input("Enter store (1/2/3): ")
        item = input("Enter item: ").title()

        try:
            quantity = int(input("Enter quantity to add: "))
            inventory = {"1": store1, "2": store2, "3": store3}.get(store)

            if inventory is None:
                print("Invalid store!")
            elif quantity <= 0:
                print("Quantity must be positive!")
            else:
                inventory[item] = inventory.get(item, 0) + quantity
                print("Stock updated successfully!")

        except ValueError:
            print("Enter a valid quantity!")

    elif choice == "7":
        print("Exiting Inventory Tracker.")
        break

    else:
        print("Invalid choice!")