n=int(input("enter no:of roes: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end='')
    for j in range(i):
        print("*",end='')
    print()
        
