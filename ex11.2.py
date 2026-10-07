days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9-10", "10-11", "11-12", "12-1"]

schedule = [["-" for _ in days] for _ in hours]

while True:
    print("\n1. View Schedule")
    print("2. Add or Overwrite Subject")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nSchedule:")
        print("Hour", *days, sep="\t")
        for i in range(len(hours)):
            print(hours[i], *schedule[i], sep="\t")

    elif choice == 2:
        row = int(input("Enter hour slot (1-4): ")) - 1
        col = int(input("Enter day (1-5): ")) - 1
        subject = input("Enter subject topic: ")

        if 0 <= row < 4 and 0 <= col < 5:
            schedule[row][col] = subject
            print("Schedule updated successfully.")
        else:
            print("Invalid selection.")

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")