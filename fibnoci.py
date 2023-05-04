def fibonacci(n):   
 n = int(input("Enter a number n to show Fibonacci series upto n:"))
a, b = 0, 1
while a < n:
        print(a, end=' ')
        a, b = b, a+b
print()


