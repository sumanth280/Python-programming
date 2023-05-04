x=[]
array=input("Enter a number:")
list=array.split(",")
for i in list:
    if(i not in x):
        x.append(i)
x.sort()
print(x)
