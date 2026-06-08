reg = int(input("If you are a registered student, enter 1 else enter 0 :"))
if reg==1:
    fee = int(input("If you already paid exam fee enter 1, else enter 0 : "))
    if fee==1:
        print("You can access the online examination")
    else:
        print("You can't access the online examination - exam fee must be paid")
else:
    print("You can't access the online examination - you must registered first")
