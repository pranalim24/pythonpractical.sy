print("Placement Eligibility Checker System")
score=float(input("Enter Your Graduation Score in(%):"))
backlogs=int(input("Enter Your Number of Backlogs="))

print("Score is:",score)
print("No.of Backlog is:",backlogs)

if score>=70 and backlogs==0:
    print("Congratulation! You Are Verify For Placement.")
else:
    print("Sorry! You Are Not Verified.")
