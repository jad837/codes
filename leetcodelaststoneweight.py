#leetcodelaststoneweight
#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/
from upperbound import range_search,first_Occurence

#arr = [2,7,4,1,8,1]
arr = [7,6,7,6,9]
#arr = [3,7,8]
q=list(arr)
q.sort()
#print(q)
while(len(q)>1):
    x,y=q.pop(),q.pop()
    if x<y:
        x,y = y,x
    res=x-y
    print(x,y,res)
    if res!=0:
        index = first_Occurence(q,res+1)
        if index==len(q)-1  :
            q.insert(index,res)
        else:
            q.insert(first_Occurence(q,res),res)
    print(q)
if len(q)<=1:
    print(-1)
print(q[0])