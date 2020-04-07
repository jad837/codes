#leetcodemedianofsortedarrays
#https://leetcode.com/problems/median-of-two-sorted-arrays/
from math import ceil
a=[1, 2]
b=[3, 4]
m=ceil( (len(a)+len(b) ) /2)-1
arr=sorted(a+b)
if len(arr)%2==0:
    print((arr[m]+arr[m+1])/2) 
else:
    print(arr[m])