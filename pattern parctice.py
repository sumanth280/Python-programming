n=int(input("enter the number: "))
for i in range(0,n):
    for j in range(i,n):
        print(" ",end='')
    for j in range (i+1):
        print("*",end='')
    print()
for i in range (0,n-1):
    for j in range(i+2):
        print(" ",end='')
    for j in range(i,n-1):
        print("*",end='')
    print()
        
