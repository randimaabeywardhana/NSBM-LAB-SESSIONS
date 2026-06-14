
marks = []
for i in range(4):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
average = total / 4
# Simple formula: GPA = average / 25 (gives scale up to 4.0)
gpa = average / 25

print("\n--- Result ---")
print(f"Total Marks: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"GPA: {gpa:.2f}")
