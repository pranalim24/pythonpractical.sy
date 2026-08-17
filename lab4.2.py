print("***Smart-Home Climate Monitoring***")

climate=input("Enter Type of Climate:").lower()

if climate=="summer":
    print("Turn on the AC")

elif climate=="winter":
    print("Please Activate the heater")

elif climate=="mansoon":
        print("Switch off the electronic devices")

else:
    print("Invalid Climate")
    print("Please Check the entered climate neatly")