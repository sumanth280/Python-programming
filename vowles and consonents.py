string=input("enter a string: ")
v=0
c=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v=v+1
    else:
        c=c+1
print("vowles are:",v)
print("consonents are:",c)
if(v>c):
    print("The vowels are maximum")
else:
    print("The consonants are maximum")
    
