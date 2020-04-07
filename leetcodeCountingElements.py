#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/


arr=[1,1,2,2]
n=len(arr)
arr.sort()
i=0
c=0
while(i<n):
    tc=1
    while(i<n-1 and arr[i]==arr[i+1]):
        #print(arr[i])
        tc+=1
        #print(i)
        i+=1
    #print(arr[i],arr[i+1])
    if i<n-1 and arr[i+1]==arr[i]+1:
        c+=tc
    i+=1

print(c)