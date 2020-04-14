#leetcodeSearch Insert Position
#https://leetcode.com/problems/search-insert-position/
from math import ceil
def binary_search(arr,l,r,key):
    middle=0
    while(l<=r):
        middle = l + (r-l)//2
        if arr[middle]==key:
            return middle
        elif arr[middle] < key:
            l = middle+1
        else :
            r = middle-1
    if arr[middle]>key:
        return middle
    elif arr[middle]<key:
        return middle+1

a=[1,3,5,6]
k=7
print(binary_search(a,0,len(a)-1,k))