basic = float(input("Enter basic salary: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
bonus = float(input("Enter bonus: "))
tax_percent = float(input("Enter tax percentage: "))

gross = basic + overtime_hours * overtime_rate + bonus
tax_amount = gross * tax_percent / 100
net_salary = gross - tax_amount

print("Gross Salary:", gross)
print("Tax Amount:", tax_amount)
print("Net Salary:", net_salary)
