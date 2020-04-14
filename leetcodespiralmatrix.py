#leetcodespiralmatrix
#https://leetcode.com/problems/spiral-matrix/

mat=[]
result=[]
sr,sc=0,0
n=len(mat)
if n==0:
    return []
m=len(mat[0])
while sr<m and sc<m:
    for i in range(sc,m):
        result.append(mat[sr][i])
    sr+=1
    for j in range(sr,n):
        result.append(mat[j][m-1])
    m-=1
    if sr<m :
        for i in range(m-1,sc-1,-1):
            result.append(mat[n-1][i])
    n-=1
    if sc<n:
        for i in range(n-1,sr-1,-1):
            result.append(mat[i][sc])
    sc+=1
print(result)