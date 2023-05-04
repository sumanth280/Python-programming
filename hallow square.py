r=int(input("enter the number of rows: "))
c=int(input("enter the number of columns: "))
if(r!=c):
    print("invalid")
    exit 
else:
    print("yes it can be a hallow square")
for i in range(r):
    for j in range(c):
         if(i==0 or i==r-1 or j==0 or j==c-1):
             print("*",end='')
         else:
             print(" ",end='')
    print()
