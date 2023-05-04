num=int(input("enter a number: "))
sum=0
res=0
while(num>0):
    res=num%10
    sum=sum+res
    num=num//10
    if(num%sum==0):
        print("yes it is a harshad number")
    else:
        print("no it is not a perfect number")
    
