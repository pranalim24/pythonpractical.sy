# Daily Class Schedule Grid

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

time_slots = [
    "9:00 - 10:00",
    "10:00 - 11:00",
    "11:00 - 12:00",
    "12:00 - 1:00",
    "1:00 - 2:00",
    "2:00 - 3:00"
]

# Create an empty schedule
schedule = {}

for time in time_slots:
    schedule[time] = {}
    for day in days:
        schedule[time][day] = "Free"


def display_schedule():
    print("\n" + "=" * 100)
    print("                     WEEKLY CLASS SCHEDULE")
    print("=" * 100)

    print(f"{'Time':<18}", end="")

    for day in days:
        print(f"{day:<16}", end="")

    print()
    print("-" * 100)

    for time in time_slots:
        print(f"{time:<18}", end="")

        for day in days:
            print(f"{schedule[time][day]:<16}", end="")

        print()

    print("=" * 100)


def update_schedule():
    print("\nAvailable days:")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day}")

    try:
        day_choice = int(input("Select day number: "))

        if day_choice < 1 or day_choice > len(days):
            print("Invalid day!")
            return

        day = days[day_choice - 1]

        print("\nAvailable time slots:")
        for i, time in enumerate(time_slots, 1):
            print(f"{i}. {time}")

        time_choice = int(input("Select time slot number: "))

        if time_choice < 1 or time_choice > len(time_slots):
            print("Invalid time slot!")
            return

        time = time_slots[time_choice - 1]

        print(f"\nCurrent topic: {schedule[time][day]}")

        new_topic = input("Enter new subject/topic: ")

        if new_topic.strip() == "":
            print("Topic cannot be empty.")
            return

        # Overwrite the existing topic
        schedule[time][day] = new_topic

        print("\nSchedule updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Main program
while True:

    print("\n===== CLASS SCHEDULE MENU =====")
    print("1. View Schedule")
    print("2. Add / Overwrite Subject")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_schedule()

    elif choice == "2":
        update_schedule()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
