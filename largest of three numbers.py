a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
c=int(input("Enter the value: "))
largest=0
if (a>b) and (a>c):
    largest=a
elif(b>a) and (b>c):
    largest=b
else:
    largest=c
print("The largest of three numbers is: ",largest)
