salary=float(input("Enter your salary :"))

if salary>=100000:
    bonus=salary*(15/100)
    print("Bonus = Rs.",bonus )
elif salary>=50000:
    bonus=salary*(10/100)
    print("Bonus = Rs.",bonus )
else:
    bonus=salary*(5/100)
    print("Bonus = Rs.",bonus )
