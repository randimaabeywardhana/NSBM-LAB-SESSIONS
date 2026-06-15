total = 0
i=1
while i<=10:
    mark=float(input("Enter marks: "))
    total=total+mark
    i=i+1
avg=total/10
print("Total is marks : ",total)
print("Avarage is : ",avg)

if avg<50:
    print ("Fail")
else:
    print ("Pass")
