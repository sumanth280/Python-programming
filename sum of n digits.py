sum=0
n=int(input("enter digits: "))
N=int(input("enter the digits required: "))
array=list(map(int,input("enter digits in array: ").strip().split()))
print(len(array))
if(N!=len(array)):
    exit(0)
else:
    for i in range(0,len(array)):
        sum=sum+array[i]
print(sum)
        
    
