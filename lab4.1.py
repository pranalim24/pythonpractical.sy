print("***Order-Tracking Simulation System***")

status=input("Enter Your Status=")

if status=="shipped":
    print("Your item is packed will deliver soon")

elif status=="delivered":
    print("Your item is delivered successfully!!")

elif status=="pending":
    print("Your item is on update will accept soon!!")  

else:
    print("Invalid Status")
    print("Check Your Status keyword neatly")
