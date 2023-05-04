import statistics
data=list(map(int,input("enter elements: ").strip().split()))
x=statistics.mean(data)
print("mean is : ",x)
