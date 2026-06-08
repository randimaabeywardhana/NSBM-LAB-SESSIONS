salary = float(input("Enter your monthly salary :"))
if salary>=50000:
    credit = int(input("Enter your credit score : "))
    if credit>=700:
        print("You can apply for bank loan")
    else:
        print("You can't apply for bank loan - not enough credit")
else:
    print("You can't apply for bank loan - salary must be 50,000 or above")
