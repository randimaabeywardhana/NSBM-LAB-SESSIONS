distance = float(input("Enter distance (km): "))
efficiency = float(input("Enter fuel efficiency (km per liter): "))
fuel_price = float(input("Enter fuel price per liter: "))
tolls = float(input("Enter highway charges: "))

fuel_used = distance / efficiency
fuel_cost = fuel_used * fuel_price
total_cost = fuel_cost + tolls

print("Fuel Used:", fuel_used, "liters")
print("Fuel Cost:", fuel_cost)
print("Final Trip Cost:", total_cost)