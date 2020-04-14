#leetcodeluckynumbersmatrix
#https://leetcode.com/problems/lucky-numbers-in-a-matrix/


matrix= [[3,7,8],[9,11,13],[15,16,17]]
matrix=[[7,8],[1,2]]
n=len(matrix)
m=len(matrix[0])
min_row=[]
max_col=[0]*m
#print(type(matrix[0][0]))
for i in range(n):
    min_r=(10**5)+5
    for j in range(m):
#        print(i,j)
        if min_r > matrix[i][j]:
            min_r = matrix[i][j]
        if max_col[j] < matrix[i][j]:
            max_col[j] = matrix[i][j]
    min_row.append(min_r)
result=[]
for i in max_col:
    if i in min_row:
        result.append(i)
print(result)