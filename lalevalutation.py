#lalevalutation.py
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/lal-evaluation/

n,k=map(int,input().split())
arr = list(map(int,input().split()))
d={}
j=0
pair=0
for i in range(n):
    if arr[i] in d:
        d[arr[i]]+=1
    else:
        d[arr[i]]=1
ans=0
print(d)
for key,value in d.items():
    if k-key in d :
        #print(key,k-key,value,d[k-key])
        if key == k-key:
            ans = ans + (value*(value-1))//2
        else:
            ans=ans+ d[k-key]*value
        d[k-key]=0
        d[key]=0
print(ans)
