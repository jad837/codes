nums=[2,3,3,2,4]

m=nums[-1]
for i in range(len(nums)-2,-1,-1):
    print(i)
    if nums[i]>m:
        nums[i]=nums[i+1]
        print(nums[i],nums[i+1])
        break
    m=min(m,nums[i])
print(nums)
flag=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:    
        flag= (False)

print (flag)