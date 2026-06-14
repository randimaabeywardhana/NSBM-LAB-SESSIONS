ticket = float(input("Enter ticket price: "))
baggage = float(input("Enter baggage fee: "))
tax = float(input("Enter airport tax: "))
hotel = float(input("Enter hotel booking charge: "))

total = ticket + baggage + tax + hotel

print("Ticket Price:", ticket)
print("Baggage Fee:", baggage)
print("Airport Tax:", tax)
print("Hotel Booking:", hotel)
print("Total Travel Cost:", total)
