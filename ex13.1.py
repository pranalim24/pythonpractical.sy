inventory = {
    "Laptop": 10,
    "Mouse": 15,
    "Keyboard": 8,
    "Headphones": 5
}

item = input("Enter item sold: ")
quantity = int(input("Enter quantity sold: "))

if item in inventory:
    if quantity <= inventory[item]:
        inventory[item] -= quantity
        print("Sale completed.")
        print("Remaining stock:", inventory[item])

        if inventory[item] == 0:
            print("Warning: Stock has dropped to zero.")
    else:
        print("Insufficient stock.")
else:
    print("Item not found.")

print("Updated Inventory:")
for item, stock in inventory.items():
    print(item, ":", stock)