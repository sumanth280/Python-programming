a=int(input('Enter a: '))
b=int(input('Enter b: '))
if(a<b):
    for i in range(a,b):
        factor=0
        for j in range(1,i):
          if i%j==0:
            factor=j
        if factor>1:
          print (i)
elif(a==b):
    print("not found any composite numbers")
elif(a==0 and b==0):
    print("0")
else:
    print("invalid")
