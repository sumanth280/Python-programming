try:
    a=int(input("enter a number:"))
    f=1
    if(a.startswith("-")):
       print('enter a positive number')
    else:
     for i in range(1, a+1):
        f=f*i
    print("factorial of",a,"=",f)
except:
    print("enter a positive integer value")
