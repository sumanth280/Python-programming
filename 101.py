n=10
list=[]
def Count(str):
 upper, lower, number, special = 0, 0, 0, 0
 for i in range(len(str)):
     if str[i].isupper():
         upper += 1
     elif str[i].islower():
         lower += 1
     elif str[i].isdigit():
         number += 1
     else:
         special += 1
 print('Upper case letters:', upper)
 print('Lower case letters:', lower)
 print('Number:', number)
 print('Special characters:', special)
for i in range(0,n):
    C=input("enter char: ")
    if(C=="*"):
        break;
    else:
        list.append(C)
Count(list)

