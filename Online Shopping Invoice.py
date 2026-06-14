
p1 = float(input("Enter price of product 1: "))
q1 = int(input("Enter quantity of product 1: "))
p2 = float(input("Enter price of product 2: "))
q2 = int(input("Enter quantity of product 2: "))
p3 = float(input("Enter price of product 3: "))
q3 = int(input("Enter quantity of product 3: "))
delivery = float(input("Enter delivery charge: "))
discount_percent = float(input("Enter discount percentage: "))

subtotal = p1*q1 + p2*q2 + p3*q3
discount = subtotal * discount_percent / 100
total = subtotal - discount + delivery

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Delivery Charge:", delivery)
print("Total Bill:", total)
