print("***Student Scholarship Eligibility Checker System***")
age=int(input("Enter Your Age:"))
income=float(input("Enter In Annual Income In Indian Rupees:"))
cast=input("Enter Your Cast:").upper()

print("Age is:",age)
print("Income is:",income)
print("Cast is:",cast )

if age<25 and income<300000 and cast in  ["SC", "OBC" ,"ST"]:
    print("Congratulations! You Are Eligible For Scholarship")
else:
    print("Sorry! You Are Not Eligible For Scholarship")