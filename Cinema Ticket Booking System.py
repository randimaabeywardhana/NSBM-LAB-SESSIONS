adult = int(input("Enter number of adult tickets: "))
child = int(input("Enter number of child tickets: "))
adult_price = float(input("Enter adult ticket price: "))
child_price = float(input("Enter child ticket price: "))
snack = float(input("Enter snack package cost: "))

adult_total = adult * adult_price
child_total = child * child_price
total_payment = adult_total + child_total + snack

print("Adult tickets total:", adult_total)
print("Child tickets total:", child_total)
print("Snack cost:", snack)
print("Total Payment:", total_payment)
