n=int(input("enter no.ofrows:"))
for i in range(n):
        for j in range(i+1):
            print ('1',end=' ')
        print()
for i in range(n-1):
        for j in range(i,n,n-1):
            print('*',end=' ')
        print()
