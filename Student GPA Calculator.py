m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))

total = m1 + m2 + m3 + m4
average = total / 4
gpa = average / 25   # simple formula

print("Total Marks:", total)
print("Average:", average)
print("GPA:", gpa)