print("===== BILLING SUMMARY =====")

purchase_amount = float(input("Enter total purchase amount: "))
discount_percent = float(input("Enter discount percentage: "))


discount_amount = (purchase_amount * discount_percent) / 100


final_amount = purchase_amount - discount_amount


print("\n========== BILL ==========")
print(f"Purchase Amount : ₹{purchase_amount:.2f}")
print(f"Discount        : {discount_percent:.2f}%")
print(f"Discount Amount : ₹{discount_amount:.2f}")
print("--------------------------")
print(f"Final Payable   : ₹{final_amount:.2f}")
print("==========================")