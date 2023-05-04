up=""
lo=""
sp=""
sc=""
s=[" "]
ch=input("enter a word: ")
for i in ch:
    if (i.islower()):
        lo=lo+i
    elif(i.isupper()):
        up=up+i
    elif(i in s):
        sp=sp+i
    else:
        sc=sc+i
u=len(lo)
v=len(up)
x=len(sp)
z=len(sc)
print("no of lowercases are:",u)
print("no of uppercases are:",v)
print("special characters are :",sc)
print("no of special characters:",z)
print("no of spaces:",x)
