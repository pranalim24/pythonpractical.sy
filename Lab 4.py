print("***Trafic Signal Rule***")


signal=input("Enter the signal colour:").lower()   #for uppercase to lowercase
#we can you uppercase() too

if signal == "red":
    print("Action:Stop")
elif signal == "yellow" :
    print("Action:Get Ready")
elif signal == "green" :
 print("Action:Go")
else:
   print("Invalid Colour")
   print("Enter Red,Green,Yellow")