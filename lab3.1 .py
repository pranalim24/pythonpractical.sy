print("***Student Scholarship Eligibility Checker System***")
age=int(input("Enter Your Age:"))
income=float(input("Enter In Annual Income In Indian Rupees:"))

print("Age is:",age)
print("Income is:",income)
if age<25 and income<300000:
    print("Congratulations! You Are Eligible For Scholarship")
else:
    print("Sorry! You Are Not Eligible For Scholarship")