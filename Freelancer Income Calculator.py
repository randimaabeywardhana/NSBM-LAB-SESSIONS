projects = int(input("Enter number of projects: "))
payment_per = float(input("Enter payment per project: "))
commission_percent = float(input("Enter platform commission percentage: "))
tax_percent = float(input("Enter tax percentage: "))

gross = projects * payment_per
commission = gross * commission_percent / 100
after_commission = gross - commission
tax = after_commission * tax_percent / 100
net = after_commission - tax

print("Gross Income:", gross)
print("Platform Commission:", commission)
print("Tax:", tax)
print("Net Income:", net)
