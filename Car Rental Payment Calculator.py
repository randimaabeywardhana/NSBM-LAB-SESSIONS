daily_fee = float(input("Enter daily rental fee: "))
days = int(input("Enter number of rental days: "))
fuel = float(input("Enter fuel charges: "))
insurance = float(input("Enter insurance fee: "))

total = daily_fee * days + fuel + insurance

print("Rental:", daily_fee * days)
print("Fuel Charges:", fuel)
print("Insurance Fee:", insurance)
print("Total Payment:", total)
