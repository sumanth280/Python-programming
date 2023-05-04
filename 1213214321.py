n=int(input("enter no:of rows: "))
for i in range(n):
    for j in range(i+1,0,-1):
        print(j,end='')
    print()
