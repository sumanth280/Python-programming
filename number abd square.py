t=[]
ur=int(input("enter a number: "))
lr=int(input("enter a number: "))
for i in range(ur,lr+1):
    if(ur<lr):
        v=(i,i**2)
        t.append(v)
print(t)
