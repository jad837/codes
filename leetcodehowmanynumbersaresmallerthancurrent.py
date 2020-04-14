#leetcodehowmanynumbersaresmallerthancurrent
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from collections import Counter
nums = [8,1,2,2,3]
n=len(nums)
nums.sort()
result=[0]*n
c= Counter(nums)
print(c)
 