total_user=int(input("enter the total user: "))
if(total_user >0):
    print(total_user)
else:
    print("invalid")
    exit(0)
staf_user=int(input("enter the staf user: "))
non_teachingstaf=staf_user/3
student_user=total_user-staf_user-non_teachingstaf
if (student_user >0):
    print(student_user)
else:
    print("invalid")
 
