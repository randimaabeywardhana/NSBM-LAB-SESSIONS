duration = float(input("Enter exercise duration (minutes): "))
cal_per_min = float(input("Enter calories burned per minute: "))
bonus = float(input("Enter additional workout bonuses: "))

total_calories = duration * cal_per_min + bonus

print("Base Calories Burned:", duration * cal_per_min)
print("Bonus Calories:", bonus)
print("Total Calories Burned:", total_calories)
