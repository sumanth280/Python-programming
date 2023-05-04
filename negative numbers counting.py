list1 =[]
n=int(input("enter no of numbers:"))
for i in range(n):
 m=int(input("enter no of numbers:"))
 list1.append(m)
pos_count, neg_count = 0, 0
for num in list1:
	if num >= 0:
		pos_count += 1

	else:
		neg_count += 1
		
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
