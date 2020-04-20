#leetcodesortmatrixdiagonally
#https://leetcode.com/problems/sort-the-matrix-diagonally/
from matrix_traversal import PrintMatrix

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

row=len(mat)
col=len(mat[0])
for i in range(col-1,-1,-1):
    j=i
    r=0
    arr=[]
    #print(j,row,col)
    while(r<row and j<col):
        #print(i)
        arr.append(mat[r][j])
        j+=1
        r+=1
    arr.sort()
    #arr.sort()
    print(arr)
    j=i
    r=k=0

    while(r<row and j<col):
        mat[r][j] = arr[k]
        j+=1
        k+=1
        r+=1
for i in range(1,row):
    j=i
    c=0
    arr=[]
    while(j<row and c<col):
        arr.append(mat[j][c])
        j+=1
        c+=1
    arr.sort()
    j=i
    k=0
    c=0
    while(j<row and c<col):
        mat[j][c] = arr[k]
        j+=1
        c+=1
        k+=1
    print(arr)
PrintMatrix.TwoDMatrix(mat)