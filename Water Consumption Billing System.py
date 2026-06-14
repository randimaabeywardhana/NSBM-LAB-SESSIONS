liters = float(input("Enter water usage (liters): "))
price_per_liter = float(input("Enter price per liter: "))
maintenance = float(input("Enter maintenance fee: "))
tax_percent = float(input("Enter tax percentage: "))

water_cost = liters * price_per_liter
tax = water_cost * tax_percent / 100
total = water_cost + maintenance + tax

print("Water Cost:", water_cost)
print("Maintenance Fee:", maintenance)
print("Tax:", tax)
print("Total Bill:", total)
