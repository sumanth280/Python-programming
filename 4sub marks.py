python=int(input("enter python marks"))
if(python<=100 and python>=0):
    print(python)
else:
    print("valid marks")
    exit(0)
c =int(input("enter c marks"))
if(c<=100 and c>=0):
    print(c)
else:
    print("valid marks")
    exit(0)
maths=int(input("enter maths marks"))
if(maths<=100 and maths>=0):
    print(maths)
else:
    print("valid marks")
    exit(0)
physics=int(input("enter physics marks"))
if(physics<=100 and physics>=0):
    print(physics)
else:
    print("valid marks")
    exit(0)
total=python+c+physics+maths
print(total)
avg=total*100
percentage=avg/400
print(percentage)
if(percentage>75):
   print("distintion")
elif(percentage>=60 and percentage<75):    
       print("first division")
elif(percentage>=50 and percentage<60):
            print("second division")
elif(percentage>=40 and percentage<50):
                print("third division")
else:
    print("fail")

