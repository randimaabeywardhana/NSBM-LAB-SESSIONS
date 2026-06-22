i=0
while i<5:
    unit=int(input("Enter electricity units:"))
    if unit>200:
        bill=unit*20
    elif unit>100:
        bill=(100*10)+(unit-100)*15
    else:
        bill=unit*10
    print ("Total bill amount is ",bill)
    i=i+1
    
