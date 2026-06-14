meal = float(input("Enter meal price: "))
beverage = float(input("Enter beverage price: "))
dessert = float(input("Enter dessert price: "))
service_percent = float(input("Enter service charge percentage: "))
tax_percent = float(input("Enter tax percentage: "))

subtotal = meal + beverage + dessert
service_charge = subtotal * service_percent / 100
tax = subtotal * tax_percent / 100
total_bill = subtotal + service_charge + tax

print("Subtotal:", subtotal)
print("Service Charge:", service_charge)
print("Tax:", tax)
print("Total Bill:", total_bill)
