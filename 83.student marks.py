math=int(input("enter math marks: "))
sci=int(input("enter sci marks: "))
py=int(input("enter py marks: "))
phy=int(input("enter phy marks: "))
if(math<0 or sci<0 or py<0 or phy<0 or math>100 or sci>100 or py>100 or phy>100 ):
    exit(0)
else:
    total=math+sci+py+phy
    per=total*0.04
    
if(per>75):
    print("distinction")
elif(60>=per and per<75):
    print("first division")
elif(50>=per and per<50):
    print("third division")
else:
    print("fail")
    
