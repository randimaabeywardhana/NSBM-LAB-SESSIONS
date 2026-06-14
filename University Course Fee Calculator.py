modules = int(input("Enter number of modules: "))
fee_per_module = float(input("Enter fee per module: "))
library_fee = float(input("Enter library fee: "))
registration_fee = float(input("Enter registration fee: "))

module_total = modules * fee_per_module
semester_fee = module_total + library_fee + registration_fee

print("Module Fees:", module_total)
print("Library Fee:", library_fee)
print("Registration Fee:", registration_fee)
print("Total Semester Fee:", semester_fee)
