a=0
b=1
n=int(input("enter the number of terms required: "))
if(n<=0):
    print("enter a valid number")
else:
  for i in range(0,n):
    print(a)
    c=a+b
    a=b
    b=c
