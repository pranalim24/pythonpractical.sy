print("***Trafic Signal Rule***")


signal=input("Enter the signal colour:").lower()   #for uppercase to lowercase


if signal == "red":
    print("Action:Stop")
elif signal == "yellow" :
    print("Action:Wait")
elif signal == "green" :
 print("Action:Go")
else:
   print("Invalid Colour")