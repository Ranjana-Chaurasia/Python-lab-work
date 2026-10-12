# Dynamic Phonebook and Contact Directory Manager
contacts = {}
print("-----Dynamic Phonebook and Contact Directory Manager-----")
while True:
    print("\n1. Add a contact")
    print("2. Display all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Remove a contact")
    print("6. Exit")
    option = input("\nEnter a choice: ")

    if option == "1":
        name = input("\nEnter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = {"phone": phone}

    elif option == "2": 
        if not contacts:
            print("No contacts added yet.")
        else:
            print("\n-----All Contacts-----")
            for name, details in contacts.items():
                print("Name: ", name)
                print("Phone: ", details["phone"])

    elif option == "3":
        search = input("\nEnter the name to search: ")
        matches = [name for name in contacts if search.lower() in name.lower()]
        if matches:
            print("Matching contacts: ", matches)
        else:
            print("No matching contacts found.")

    elif option == "4":
        update = input("\nEnter the contact name to update: ")
        if update in contacts:
            phone = input("Enter the new phone number: ")
            contacts[update]["phone"] = phone
        else:
            print("This person is not in your contact.")

    elif option == "5":
        name = input("\nEnter the contact name to remove: ")
        if name in contacts:
            contacts.pop(name, None)
        else:
            print("This person is already not in your contact.")
    
    elif option == "6":
        print("\nExiting the program :)")
        break

    else:
        print("Invalid choice. Try again.")