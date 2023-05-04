name=input("enter the name:")
reg=int(input("enter the reg no:"))
m1=int(input("enter sub1 marks:"))
m2=int(input("enter sub2 marks:"))
m3=int(input("enter sub3 marks:"))
m4=int(input("enter sub4 marks:"))
m5=int(input("enter sub5 marks:"))

total=m1+m2+m3+m4+m5
avg=total/5
percentage=(total/5)*100

if(percentage>50):
    print("grade c")
elif(percentage<80):
    print("grade b")
else:
    print("grade a")


print("name",name)
print("reg.no",reg)
print("total:",total)
print("average:",avg)
print("percentage:",percentage)
