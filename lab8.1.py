prices = [1250.50, 4500.75, 2300.25, 7800.90, 3200.40, 1500.60]

prices.sort(reverse=True)


print("Sorted Prices:", prices)
print("Top 3 Priciest Entries:")

for price in prices[:3]:
    print(price)