print("===== GROCERY BILL =====")

# Accept details of three items
name1 = input("Enter name of item 1: ")
qty1 = int(input("Enter quantity: "))
price1 = float(input("Enter price per item: "))

name2 = input("Enter name of item 2: ")
qty2 = int(input("Enter quantity: "))
price2 = float(input("Enter price per item: "))

name3 = input("Enter name of item 3: ")
qty3 = int(input("Enter quantity: "))
price3 = float(input("Enter price per item: "))


amount1 = qty1 * price1
amount2 = qty2 * price2
amount3 = qty3 * price3


total = amount1 + amount2 + amount3


print("\n========== FINAL BILL ==========")
print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Amount':<10}")
print("-" * 43)
print(f"{name1:<15}{qty1:<8}{price1:<10.2f}{amount1:<10.2f}")
print(f"{name2:<15}{qty2:<8}{price2:<10.2f}{amount2:<10.2f}")
print(f"{name3:<15}{qty3:<8}{price3:<10.2f}{amount3:<10.2f}")
print("-" * 43)
print(f"{'Total Bill':<33}{total:.2f}")
print("================================")