L=[]
m=[]
n=int(input("enter an element: "))
for i in range(0,n):
    num=input("enter numbers in list: ")
    L.append(num)
L.sort()
for i in L:
    if(i not in m):
        m.append(i)
print(m)
