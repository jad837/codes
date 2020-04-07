#Roy and Symmetric Logos
#https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/roy-and-symmetric-logos-1/

from math import ceil
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    mat=[]
    for i in range(n):
        rows=input()
        mat.append(rows)
    middle = ceil(n/2)
    print(middle)
    print(mat)
    flag=True
    for i in range(middle):
        for j in range(middle):
            if mat[i][j] != mat[i][middle+j] or mat[i][j] != mat[middle+i][middle+j] or mat[i][j] != mat[middle+i][j]:
                print("coordinates")
                print(i,j,middle+i,middle+j)
                print(mat[i][j])
                print(mat[i][middle+j])
                print(mat[middle+i][middle+j])
                print(mat[middle+i][j])
                print(middle+j)
                print(middle+i)                
                flag=False
                break
        if flag==False:
            break
    if flag and n%2!=0:
        for i in range(n):
            if mat[middle][i]!=mat[middle][n-i-1]:
                flag=False
                break
    if flag:
        print("YES")
    else:
        print("NO")