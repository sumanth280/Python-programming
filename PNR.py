p=int(input("enter the principle amount: "))
n=int(input("enter the no:of years: "))
if(p<0 or n<0):
    print("invalid")
    exit(0)
else:
    sr_citizen=input("enter trure or false")
    if(sr_citizen=='true'):
        intrest=p*n*12/100
    else:
        intrest=p*n*10/100
    print(intrest)
