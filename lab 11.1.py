print("!"*30)
print("Movie Theatre Booking Stimulator")
print("!"*30)

total_rows = int(input("Enter number of rows in the theatre: "))
seats_per_row = int(input("Enter number of seats per row: "))

#Movie layout
theatre_layout=[]
for r in range(total_rows):
    row = []
    for c in range(seats_per_row):
        row.append("o")       # every seat starts as Open
    theatre_layout.append(row)    # add this row into the main nested list

print(f"\nTheatre layout created: {total_rows} rows x {seats_per_row} seats per row.")
print("All seats are currently Open (O).\n")
while True:
    print("-" * 45)
    print("1. Display Bus Layout")
    print("2. Reserve a Seat")
    print("3.Exit")
    print("-" * 45)

    choice = input("Enter your choice (1-3): ").strip()

    # --------------- DISPLAY LAYOUT (Traversal) ---------------
    if choice == '1':
        print("\nCurrent Bus Layout:")
        print("(Rows top to bottom = Row 1 to Row", total_rows, ")\n")
        for r in range(len(theatre_layout)):       # traverse outer list (rows)
            print(f"Row {r + 1}: ", end="")
            for c in range(len(theatre_layout[r])):    # traverse inner list (seats)
                print(theatre_layout[r][c], end=" ")
            print()
        print()

    # --------------- RESERVE SEAT ---------------
    elif choice == '2':
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:
            if theatre_layout[row_num][col_num] == "X":
                print("This seat is already reserved!\n")
            else:
                theatre_layout[row_num][col_num] = "X"   # indexing into nested list
                print(f"Seat at Row {row_num + 1}, Seat {col_num + 1} reserved successfully.\n")
        else:
            print("Invalid row or seat number.\n")

    
    # --------------- EXIT ---------------
    elif choice == '3':
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")