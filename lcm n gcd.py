def lcm(l):    
    def find_lcm(num1, num2):
        if(num1>num2):
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while(rem != 0):
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = int(int(num1 * num2)/int(gcd))
        return lcm
    num1 = l[0]
    num2 = l[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, len(l)):
        lcm = find_lcm(lcm, l[i])
    print(lcm)
def gcd(l):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
      
        return x
    num1=l[0]
    num2=l[1]
    gcd=find_gcd(num1,num2)
      
    for i in range(2,len(l)):
        gcd=find_gcd(gcd,l[i])
          
    print(gcd)
z=[]
n=int(input())
for i in range(n):
    z.append(int(input()))
gcd(z)
lcm(z)
