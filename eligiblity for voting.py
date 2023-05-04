age=int(input("enter age of a person: "))
if(age>18):
    print("yes you are eligible for voting")
if(age>0 and age<18):
    print("you are eligible to vote after",18-age,"years")
elif(age<=0):
    print("enter valid age")
