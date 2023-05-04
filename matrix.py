r=int(input("enter the number of rows: "))
c=int(input("enter the number of columns: "))
matrix=[]
print("enter the entries row wise: ")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print(matrix)
