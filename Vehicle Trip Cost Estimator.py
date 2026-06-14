room_charge = float(input("Enter room charge per day: "))
days = int(input("Enter number of days: "))
food_charges = float(input("Enter food charges: "))
service_charge_percent = float(input("Enter service charge percentage: "))

subtotal = room_charge * days + food_charges
service_charge = subtotal * service_charge_percent / 100
total_bill = subtotal + service_charge

print("Subtotal:", subtotal)
print("Service Charge:", service_charge)
print("Total Bill:", total_bill)