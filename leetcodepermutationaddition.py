#leetcodepermutationaddition
#https://leetcode.com/problems/queries-on-a-permutation-with-key/


queries=[3,1,2,1]
m=5
d={}
for i in range(1,m+1):
    d[i]=i-1
for i in range(len(queries)):
    temp=queries[i]
    queries[i]=d[temp]
    