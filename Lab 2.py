print("***Groceery Shop Billing Calculator***")

rice_qty=float(input("Enter the quantity of rice(in kg):"))
rice_price_per_kg=60
rice_total= rice_qty*rice_price_per_kg

sugar_qty=float(input("Enter the quantity of  sugar(in kg):"))
sugar_price_per_kg=100
sugar_total= sugar_qty*sugar_price_per_kg

salt_qty=float(input("Enter the quantity of salt(in kg):"))
salt_price_per_kg=70
salt_total= salt_qty*salt_price_per_kg

oil_qty=float(input("Enter the quantity of oil(in litre):"))
oil_price_per_lit=200
oil_total= oil_qty*oil_price_per_lit

print("***Display Bill Details***")
print("rice:",rice_total)
print("sugar:",sugar_total)
print("salt:",salt_total)
print("oil:",oil_total)

Total_Bill = rice_total+sugar_total+salt_total+oil_total
print("Total Bill:", Total_Bill)

Discount=0
if Total_Bill>=2000:
    Discount=Total_Bill*0.1
    print("Discount:",Discount)

elif Total_Bill>=1000:
    Discount=Total_Bill*0.05
    print("Discount:",Discount)

else:
    print("No Discount")

Final_Bill= Total_Bill-Discount
print("Final Bill:",Final_Bill)