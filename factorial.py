n =int(input("enter a number:"))
fact=1
for i in range(1,n+1):
   if(n.isdigit()):
    fact=fact*i
    print("factorial of number is",fact)
   else:
    print("enter a valid number")
