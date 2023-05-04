income=int(input("enter the income: "))
if(income<=0):
    print("invalid")
    exit(0)
else:
    if(income<150000):
        print("no tax")
    elif(income>150001 and income<300000):
        tax=income*0.1
        print(tax)
    elif(income>3000001 and income<500000):
        tax=income*0.2
        print(tax)
    elif(income>500001):
        tax=income*0.3
        print(tax)
    else:
        print("invalid")

    
