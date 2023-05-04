n=int(input("enter the no:of rows: "))
p=int(input("enter a number: "))
for i in range(n+1):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print(p+1,end=" ")
    p=p-1
    print()
        
    
