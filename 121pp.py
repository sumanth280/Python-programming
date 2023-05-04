n=int(input("enter no:of rows: "))
m=int(input("enter element to be printed: "))
for i in range(n):
       for j in range(i+1):
           print(m,end='')
       print()
for i in range(n-1):
    for j in range(i,n-1):
        print(m,end='')
    print()
