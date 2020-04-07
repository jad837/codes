#leetcode Maximize Sum Of Array After K Negations
#https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
from math import ceil
def binarySearch(arr):
    m=ceil(len(arr)/2)
a=[4,2,3]
k=1
#a=[-4,-6,9,-2,2]
#k=4

#a = [3,-1,0,2]
#k = 3
#a=[3,-1,0,2]
#k=3
#a = [2,-3,-1,5,-4]
#k=2

a.sort()
i=0
#print(a)
while i>=0 and a[i]<0 and k>0:
    a[i]*=-1
    i+=1
    k-=1
print(a)
if a[i]==0:
    print(sum(a)) 
if k>0 :
    index = a.index(min(a))
    if k%2!=0:
        a[index]*=-1
#        print(sum(a))

#        print(sum(a))
print(sum(a))