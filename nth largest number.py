list=[14,67,48,23,5,62]
list.sort(reverse=True)
print(list)
n=input("enter nth largest number: ")
if(n.isnumeric()):
    n=int(n)
    print("max number",list[n-1])
else:
    print("enter a number")
list.sort()
print(list)
n=input("enter nth minimum number: ")
if(n.isnumeric()):
    n=int(n)
    print("min number",list[n-1])
else:
    print("enter a number")
