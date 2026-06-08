log = (input("Are you logged in (yes/no):"))
if log=="yes":
    cart = int(input("Enter your cart vaue : "))
    if cart>1000:
        payment = (input("Is payment succesfull? (yes/no) :"))
        if payment=="yes":
            print("Oder Confirmed")
        else:
            print("Oder can't confirm - need payment successfull")
    else:
        print("Oder can't confirm - not enough cart value")    
else:
    print("Oder can't confirm - you must logged in")
