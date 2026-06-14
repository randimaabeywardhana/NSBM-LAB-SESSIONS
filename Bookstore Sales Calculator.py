p1 = float(input("Enter price of book 1: "))
q1 = int(input("Enter quantity of book 1: "))
p2 = float(input("Enter price of book 2: "))
q2 = int(input("Enter quantity of book 2: "))
p3 = float(input("Enter price of book 3: "))
q3 = int(input("Enter quantity of book 3: "))
discount_percent = float(input("Enter membership discount percentage: "))
delivery = float(input("Enter delivery charge: "))

subtotal = p1*q1 + p2*q2 + p3*q3
discount = subtotal * discount_percent / 100
final_payment = subtotal - discount + delivery

print("Subtotal:", subtotal)
print("Membership Discount:", discount)
print("Delivery Charge:", delivery)
print("Final Payment:", final_payment)
