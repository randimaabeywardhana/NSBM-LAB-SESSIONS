hall = float(input("Enter hall rental: "))
deco = float(input("Enter decoration cost: "))
food_per_person = float(input("Enter food cost per person: "))
guests = int(input("Enter number of guests: "))
sound = float(input("Enter sound system rental: "))

total = hall + deco + food_per_person * guests + sound

print("Hall:", hall)
print("Decoration:", deco)
print("Food:", food_per_person * guests)
print("Sound System:", sound)
print("Total Budget:", total)
