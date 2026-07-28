print("***Student  Eligibility Critaria for Admission***")

name=input("Enter Student Name:")
marks=float(input("Enter Student Marks/Percentage:"))
age=int(input("Enter Student Age:"))

print("Admission Result")
print("*****")

if marks>=50:
    if age>= 17:
        if marks>=90:
            print(name,"Admission Approved")
            print("Cousre Alloted:Computer Science And Enggineering")
            print(name,"Congratulation you have get Scholarship:100%")
        elif marks>=75:
            print(name,"Admission Approved")
            print("Cousre Alloted:Information Technology")
            print(name,"Congratulation you have get Scholarship:50%")
        elif marks>=60:
            print(name,"Admission Approved")
            print("Cousre Alloted:Artifical Intellgence")
            print(name,"Congratulation you have get Scholarship:25%")
        else:
            print(name,"Admission Approved")
            print("Cousre Alloted:Electrical Engineering")
            print(name,"No Scholarship")       
else:
    print(name,"Admission Rejected")
    print(" No Cousre Alloted")
    print("Reason:Minimum Marks should be above 50%")
    print("Reason:Minimum Age should be above 17")            
