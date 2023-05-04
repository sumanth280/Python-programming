n=[]
p=[]
r=input("enter a number: ")
s=int(r)
if (s>0):
    n.append(s)
    sum_n=sum(n)
    len_n=len(n)
    avg_n=sum(n)/len(n)
else:
    avg_n=0
if (s<0):
    p.append(s)
    sum_p=sum(p)
    len_p=len(p)
    avg_p=sum(n)/len(n)
else:
    avg_n=0
print("avg positive numbers:",avg_n)
print("avg negative numbers:",avg_p)
    
