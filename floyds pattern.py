n=int(input())
k=1
for i in range (1,n+1):
    for x in range(1,(n-i)+1):
        print(" ",end="")
    for j in range(0,i):
        if(j==0):
            k=1
        else:
            k=k*(i-j)//j
        print(k,end=" ")
    print()
