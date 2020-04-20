mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
m=len(mat)
n=len(mat[m-1])
for i in range(m):
    s=0
    for j in range(n):
        s+=mat[i][j]
        mat[i][j]=s
