bal=50000
withdraw=0
withdrawamount=0
withdrawcount=0

while withdraw!=-1 or bal==0:
    withdraw=float(input("Enter your withdrawal amount (Rs.) :"))
    if bal>withdraw:
        bal=bal-withdraw
        withdrawamount=withdrawamount+withdraw
        withdrawcount=withdrawcount+1
    else:
        print("Insufficient Balance")
print("The remaining balance is ",bal)
print("The total amount of withdrawal is ",withdrawamount)
print("Number of successful withdrawals ",withdrawcount)
    
    
    
    
    
