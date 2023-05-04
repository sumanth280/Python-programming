n=int(input("enter a number: "))
if(n>0):
    sqrt=n**0.5
    print(sqrt)
    sq=sqrt*sqrt
    print(sq)
    if(n!=sq):
        print("enter a perfect number")
        exit(0)
    else:
        print("square root is: ",sqrt)
        
else:
    print("enter a number")
    
