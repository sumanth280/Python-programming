import statistics
data=list(map(int,input("enter elements: ").strip().split()))
x=statistics.mode(data)
print("mean is : ",x)
