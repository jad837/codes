#leetcodeweaketsrowinmatrix
#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

rows=[0]*len(mat)
n=len(mat)
for i in range(n):
    s=0
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            s+=1
    rows[i]=[i,s]
rows.sort(key= lambda x:x[1])
resultset=[]
for i in range(k):
    resultset.append(rows[i][0])
print(resultset)