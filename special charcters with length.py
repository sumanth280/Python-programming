up=""
lo=""
sp=""
sc=""
dig=""
s=[" "]
ch=input("enter a word: ")
for i in ch:
    if (i.islower()):
        lo=lo+i
    elif(i.isupper()):
        up=up+i
    elif(i.isdigit()):
        num=num+1
    elif(i in s):
        sp=sp+i
    else:
        sc=sc+i
z=len(sc)
print("special characters",sc)
print("no of special characters",z)

