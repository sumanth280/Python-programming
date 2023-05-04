L=[]
n=int(input("enter the no:of integers: "))
for i in range(0,n):
    num=input("enter a number: ")
    num=int(num)
    L.append(num)
L.sort()
print(L)
print(max(L))
