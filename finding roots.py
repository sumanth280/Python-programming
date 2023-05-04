a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
d=b*b-4*a*c
if(d==0):
    print("roots are real and equal")
elif(d>0):
    print("roots are different and equal")
else:
    print("roots are imaginary")
