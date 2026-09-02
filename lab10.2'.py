products = ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"]

print("Available Products:", products)

item = input("Enter product name to search: ")

if item in products:
    index = products.index(item)
    print("Item found!")
    print("Product:", item)
    print("Index:", index)
else:
    print("Item not found in inventory.")