students = {
    101: "student101@gmail.com",
    102: "student102@gmail.com",
    103: "student103@gmail.com",
    104: "student104@gmail.com",
    105: "student105@gmail.com"
}

roll_id = int(input("Enter student roll number: "))

if roll_id in students:
    print("Email Address:", students[roll_id])
else:
    print("Student roll number not found.")
    