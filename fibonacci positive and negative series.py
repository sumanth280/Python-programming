a=0
b=1
choice=int(input("enter the choice:"))
n=int(input("nth febnoci series: "))
for i in range(1,n+1):
   if(choice==1):
    print(a)
    c=a+b
    a=b
    b=c
   elif(choice==2):
    print(a)
    c=a-b
    a=b
    b=c
   else:
      print("invalid choice")
    
