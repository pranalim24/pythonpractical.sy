products = input("Enter product labels separated by commas: ").split(",")

products = [product.strip() for product in products]

item = input("Enter item name to search: ").strip()

if item in products:
    index = products.index(item)
    print("Item found.")
    print("Index location:", index)
else:
    print("Item not found.")