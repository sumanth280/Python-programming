a=str(input("enter the name of the file with text extension: "))
file2=open(a,'r')
line=file2.readline()
while(line!=" "):
    print(line)
    line=file.readline()
file2.close()
