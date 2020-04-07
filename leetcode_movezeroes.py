#movezeros
#https://leetcode.com/problems/move-zeroes/
'''
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
'''
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[count]=arr[i]
        count+=1
    while count <len(arr):
        arr[count]=0
        count+=1
print(arr)
'''
nums=list(map(int,input().split()))
#print(nums)
count = 0 
n=len(nums)
for i in range(n): 
    print(nums)
    if nums[i] != 0: 
        nums[count] = nums[i] 
        count+=1
while count < n: 
    nums[count] = 0
    count += 1
print(nums)
