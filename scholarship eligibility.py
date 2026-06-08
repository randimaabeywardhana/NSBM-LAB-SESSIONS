mark = float(input("Enter your mark :"))
if mark>=75:
    income = float(input("Enter your family monthly income : "))
    if income <50000:
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship - income must be less than 50,000 ")
else:
    print("Not Eligible for scholarship - Marks must be 75 or above")
