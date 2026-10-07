print("===== DAILY EXPENSE TRACKER =====")

total_expense = 0
expense_count = 0

while True:
    expense = float(input("Enter daily expense amount (Enter 0 to stop): "))

    if expense == 0:
        break

    total_expense += expense
    expense_count += 1

print("\n===== MONTHLY EXPENSE SUMMARY =====")
print(f"Total Monthly Expenditure : ₹{total_expense:.2f}")
print(f"Number of Expenses        : {expense_count}")
print("===================================")