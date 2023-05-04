sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
total=sub1+sub2+sub3+sub4+sub5
print("total",total)
percentage = total/5
print("percentage",percentage)
if(percentage>=80):
    print("grade A")
elif(percentage>=50&percentage<80):
    print("grade B")
elif (percentage<50):
    print("grade C")
