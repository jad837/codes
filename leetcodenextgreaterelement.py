#leetcodenextgreaterelement
#https://leetcode.com/problems/next-greater-element-ii/

nums=[1,2,1]
'''
resultlist=[]
n=len(nums)
for i in range(len(nums)):
    nx=(i+1)%n
    print(nx)

    while True:
        if nums[nx]>nums[i]:
            resultlist.append(nums[nx])
            break
        nx = (nx+1)%n
        if nx==i:
            resultlist.append(-1)
            break
print(resultlist)
'''
