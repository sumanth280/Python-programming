sum=0
num=int(input("enter a number: "))
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
print("sum of factors of the number is ",sum)        
if(sum==num):
    print("so,",num,"is a perfect number")
else:
    print('so,',num,"is not a perfect number")

   
    
