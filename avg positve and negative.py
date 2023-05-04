ln=[]
lp=[]
while(True):
    s=(input("enter a number: "))
    if((s.isnumeric())or(s.startswith("-"))):
        n=int(s)
        if(n==-1):
            break
        else:
            if((n>0) and (n<100)):
                lp.append(n)
            elif((n<0) and (n>(-100))):
                ln.append(n)
            else: 
                pass
if(lp!=[]):
    sum_p=sum(lp)
    len_p=len(lp)
    avg_p=sum(lp)/len(lp)
else:
    avg_p=0
if(ln!=[]):
    sum_n=sum(ln)
    len_n=len(ln)
    avg_n=sum(ln)/len(ln)
else:
    avg_n=0
print("avg positive number: ",avg_p)
print("avg negative number: ",avg_n)
    
