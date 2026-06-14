wattage = float(input("Enter appliance wattage (watts): "))
hours_per_day = float(input("Enter hours used per day: "))
cost_kwh = float(input("Enter cost per kWh: "))

daily_kwh = wattage * hours_per_day / 1000
monthly_kwh = daily_kwh * 30
bill = monthly_kwh * cost_kwh

print("Daily Consumption (kWh):", daily_kwh)
print("Monthly Consumption (kWh):", monthly_kwh)
print("Monthly Bill:", bill)
