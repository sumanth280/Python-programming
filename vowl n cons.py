string=input("Enter the string: ")
vow=0
con=0
for i in string:
    if(i.isalpha()):
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o'
           or i == 'u'or i == 'A' or i == 'E' or i == 'I'
           or i == 'O' or i == 'U'):
            vow=vow+1
        else:
            con=con+1

print("Vowels = ",vow)
print("Consonants = ",con)
