seats = [["O" for _ in range(3)] for _ in range(3)]

print("Initial Seating Layout:")
for row in seats:
    print(*row)

row = int(input("Enter row (1-3): "))
col = int(input("Enter column (1-3): "))

row -= 1
col -= 1

if 0 <= row < 3 and 0 <= col < 3:
    if seats[row][col] == "O":
        seats[row][col] = "X"
        print("Seat reserved successfully.")
    else:
        print("Seat is already reserved.")
else:
    print("Invalid seat selection.")

print("Updated Seating Layout:")
for row in seats:
    print(*row)