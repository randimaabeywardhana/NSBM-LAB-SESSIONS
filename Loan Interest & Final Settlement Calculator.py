loan = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
months = int(input("Enter repayment period (months): "))

years = months / 12
total_interest = loan * (interest_rate / 100) * years
final = loan + total_interest
monthly = final / months

print("Total Interest:", total_interest)
print("Final Payment:", final)
print("Monthly Installment:", monthly)
