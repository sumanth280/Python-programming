x=int(input("enter value of x: "))
y=int(input("enter value of y: "))
power=x**y
add=x+y
mul=x*y
div=x/y
choice=input('enter a function')
if(choice=='power'):
    print(power)
elif(choice=='add'):
    print(add)
elif(choice=='mul'):
    print(mul)
elif(choice=='div'):
    print(div)
else:
    print("invalid")
