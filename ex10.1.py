prices = list(map(float, input("Enter asset costs separated by spaces: ").split()))

prices.sort(reverse=True)

print("Top 3 priciest entries:")

for price in prices[:3]:
    print(price)