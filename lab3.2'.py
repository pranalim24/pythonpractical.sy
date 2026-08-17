print("Placement Eligibility Checker System")
score=float(input("Enter Your Graduation Score in(%):"))
backlogs=int(input("Enter Your Number of Backlogs="))
interview=input("Enter Your Interview Status Pass/Fail:").upper()
print("Score is:",score)
print("No.of Backlog is:",backlogs)
print("Interview Status Is:", interview)
if score>=70 and backlogs==0 and interview=="PASS":
    print("Congratulation! You Are Verify For Placement.")
else:
    print("Sorry! You Are Not Verified.") 
