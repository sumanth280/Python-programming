n=int(input("enter a number: "))
for i in range(0,n):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i+1):
        print(" *",end='')
    print()
