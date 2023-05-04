import statistics
data=list(map(int,input("enter elements: ").strip().split()))
x=statistics.median(data)
print("mean is : ",x)
