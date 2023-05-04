num=int(input("Enter the Number: "))
n=num
sum=0
while(n!=0):
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10

print(sum)
if(sum==num):
    print("Armstrong")
else:
    print("not")



