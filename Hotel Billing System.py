room_charge_per_day = float(input("Enter room charge per day: "))
days = int(input("Enter number of days: "))
food_charges = float(input("Enter food charges: "))
service_charge_percent = float(input("Enter service charge percentage: "))

subtotal = room_charge_per_day * days + food_charges
service_charge = subtotal * service_charge_percent / 100
total_bill = subtotal + service_charge

print("\n--- Hotel Bill ---")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Service Charge: ${service_charge:.2f}")
print(f"Total Bill: ${total_bill:.2f}")
