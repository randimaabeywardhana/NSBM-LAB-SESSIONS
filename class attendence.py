eligible=0
noteligible=0
tot=0
avg=0
for i in range(10):
    attend=float(input("Enter the attendance percentage: "))
    if attend>=75:
        eligible=eligible+1
    else:
        noteligible=noteligible+1
    tot=tot+attend
    avg=tot/10


print("Number of students eligible for exam : ",eligible)
print("Number of students not eligible for exam : ",noteligible)
print("The average attendence of the class : ", avg)
        
     
    
