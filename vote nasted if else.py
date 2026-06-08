age = int(input("Enter your age :"))
if age>=18:
    citizen = int(input("If you are a citizen person click 1 else 0 : "))
    if citizen == 1:
        print("You are eligible to vote")
    else:
        print("Not eligible for vote - need citizen person")
else:
    print("Not eligible for vote - age must be 18 or above")
