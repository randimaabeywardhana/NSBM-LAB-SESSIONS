room = (input("Room available? (yes/no):"))
if room=="yes":
    ID =(input("Do you have valid ID? (yes/no) : "))
    if ID=="yes":
        payment = (input("Is advanced payment completed? (yes/no) :"))
        if payment=="yes":
            night = int(input("Number of nights :"))
            if night>=1:
                print ("Check in approved")
            else:
                print ("Check in not approved -  you must stay one night at least")
        else:
            print ("Check in not approved -  you must complete advanced payment")
    else:
        print ("Check in not approved -  you must have valid ID")
else:
    print ("Can't check in - Do not have available rooms")
            
        
            
