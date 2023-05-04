f=[]
n=int(input("Enter the n value: "))
nth=input("enter a number for nth values: ")
for i in range(2 ,n):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
         f.append(i)
print(f)
nth=int(nth)
c=nth+nth+1
v=nth+1
print(f[v:c])
