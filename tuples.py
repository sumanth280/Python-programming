l1=[]n1=int(input("enter a lower number:")) 
n2=int(input("enter a upper number:")) 
for i in range(n1,n2):
 s=(n1,n1**2) 
 l1.append(s) 
n1=n1+1 
n2=n2+1 
print(l1)
