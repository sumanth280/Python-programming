m=int(input("enter m : "))
n=int(input("enter n: "))
c=int(input("enter choice: "))
if(c==1):
    for i in range(1,n+1):
        print(f'{m}*{i}={m*i}')
elif(c==2):
    for i in range(1,n+1):
        print(f'{m}/{i}={m/i}')
else:
    print("invalid")
