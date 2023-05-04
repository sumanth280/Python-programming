ann=input("enter anniversery dd/mm/yyyy: ")
year=int(ann[-4: ])
leap=0
if(year%4==0 and year%100!=0):
    leap=1
    print("leap year")
else:
    leap=0
    print("not a leap year")
if(leap==1):
    year=year+1
    ann=ann[0:6]+str(year)
    print("next year anniversery: ",ann)
else:
    year=year-1
    ann=ann[0:6]+str(year)
    print("before year anniversery: ",ann)
