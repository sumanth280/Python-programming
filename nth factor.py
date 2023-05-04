total=0
num=int(input("enter a number: "))
nTH=int(input("nth factor: "))
for i in range(1,num+1):
     if(num%i==0):
         total=total+1
         if(nTH==total):
             print(i)
