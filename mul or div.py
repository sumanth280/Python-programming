choice=int(input("Choice: "))
m=int(input("M : "))
n=int(input("N : "))
if(choice==1):
    for i in range(1,n+1):
        print(f'{i}*{m}={m*i}')
elif(choice==2):
 for i in range(1,n+1):
       print(f'{i}/{m}={m/i}')
else:
    print("invalid choice")
