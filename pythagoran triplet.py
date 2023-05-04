n=int(input("enter the number :"))
if n>0:
    for a in range(1,n-1):
        for b in range(a+1,n):
            for c in range(b+1,n+1):
                if(a*a+b*b==c*c):
                    print(a,b,c)
else:
    print("WRONG NATURAL  NUMBER !!!!!")
