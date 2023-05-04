str=input("Please enter a string as you wish: ")
l=[]
m=[]
duplicates = {}
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
         vowels=vowels+1
         l.append(i)
    elif(i.isdigit()):
        continue
    else:
       consonants=consonants+1
       m.append(i)
   
print("No of vowels are:",vowels)
print("vowels are:",l)
print("No of consonants are:",consonants)
print("consonants are:",m)

for char in str:
   if char in duplicates:
      duplicates[char] += 1
   else:
      duplicates[char] = 1
print("repeated letters are:")
for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")


