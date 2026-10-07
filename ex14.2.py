phonebook = {}

while True:
    print("\n1. Add Contact")
    print("2. Display Directory")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter contact number: ")

        if name in phonebook:
            print("Contact already exists. Cannot overwrite.")
        else:
            phonebook[name] = number
            print("Contact added successfully.")

    elif choice == 2:
        print("\nPhone Directory:")
        for name, number in phonebook.items():
            print(name, ":", number)

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")