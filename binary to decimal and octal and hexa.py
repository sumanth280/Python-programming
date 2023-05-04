try:
    bin= int(input("Enter an binary number: "))
    print("The binary value of",bin,"is:")
    print(float(bin),"in decimal")
    print(oct(bin),"in octal")
    print(hex(bin),"in hexadecimal")
except:
    print("enter a valid number")
