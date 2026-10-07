print("===== MONTHLY EXPENSE TRACKER =====")

food = 0
travel = 0
shopping = 0

while True:
    print("\n1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Finish")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter Food expense: "))
        food += amount

    elif choice == 2:
        amount = float(input("Enter Travel expense: "))
        travel += amount

    elif choice == 3:
        amount = float(input("Enter Shopping expense: "))
        shopping += amount

    elif choice == 4:
        break

    else:
        print("Invalid choice!")

total = food + travel + shopping

print("\n========== MONTHLY EXPENSE SUMMARY ==========")
print(f"{'Category':<15}{'Total Expense':>15}")
print("----------------------------------------------")
print(f"{'Food':<15}₹{food:>14.2f}")
print(f"{'Travel':<15}₹{travel:>14.2f}")
print(f"{'Shopping':<15}₹{shopping:>14.2f}")
print("----------------------------------------------")
print(f"{'Total':<15}₹{total:>14.2f}")
print("==============================================")