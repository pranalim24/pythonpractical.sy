rows=int(input("Enter Number of Rows:"))

for i in range(1, rows+1):
    for j in range(i):
        print(i, end="")
    print()