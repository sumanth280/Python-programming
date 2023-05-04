

m=int(input('Enter m: '))
n=int(input('Enter n: '))
lp=[]
lc=[]
for a in range(m,n+1):
    factor=0
    for i in range(1,a):
      if a%i==0:
        factor=i
    if factor>1:
        lc.append(a)
    if factor==1:
        lp.append(a)
print("composite numbers are:",lc)
print("prime numbers are:",lp)
