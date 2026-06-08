balance=20000
pin = int(input("Enter your PIN number :"))
if pin==1234:
    withdraw = float(input("Enter your withdrawal amount : "))
    if withdraw <=balance:
        print("You can do your withdrawal")
    else:
        print("You do not have available balance")
else:
    print("Your PIN number is incorrect")
