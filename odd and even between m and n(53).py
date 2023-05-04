even=0
odd=0
o=[]
e=[]
m=int(input("enter m value: "))
n=int(input("enter n value: "))
for i in range  (m,n):
    if(i%2==0):
        even=even+1
        e.append(i)
    else:
        odd=odd+1
        o.append(i)
print(even)
print(odd)
