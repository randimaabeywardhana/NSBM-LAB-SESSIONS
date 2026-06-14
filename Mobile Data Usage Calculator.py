data_gb = float(input("Enter data usage (GB): "))
cost_per_gb = float(input("Enter cost per GB: "))
additional = float(input("Enter additional service charges: "))

data_cost = data_gb * cost_per_gb
final_bill = data_cost + additional

print("Data Cost:", data_cost)
print("Additional Charges:", additional)
print("Final Bill:", final_bill)
