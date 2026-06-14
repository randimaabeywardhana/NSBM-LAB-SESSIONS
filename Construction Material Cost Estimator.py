cement_bags = int(input("Enter number of cement bags: "))
price_per_bag = float(input("Enter price per bag: "))
sand = float(input("Enter sand cost: "))
labor = float(input("Enter labor cost: "))
transport = float(input("Enter transportation cost: "))

total = cement_bags * price_per_bag + sand + labor + transport

print("Cement Cost:", cement_bags * price_per_bag)
print("Sand Cost:", sand)
print("Labor Cost:", labor)
print("Transport Cost:", transport)
print("Total Cost:", total)
