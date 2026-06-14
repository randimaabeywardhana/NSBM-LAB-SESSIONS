monthly_fee = float(input("Enter monthly fee: "))
months = int(input("Enter number of months: "))
registration = float(input("Enter registration fee: "))
trainer_fee = float(input("Enter personal trainer fee: "))
tax_percent = float(input("Enter tax percentage: "))

before_tax = monthly_fee * months + registration + trainer_fee
tax = before_tax * tax_percent / 100
final_payment = before_tax + tax

print("Total Before Tax:", before_tax)
print("Tax:", tax)
print("Final Payment:", final_payment)
