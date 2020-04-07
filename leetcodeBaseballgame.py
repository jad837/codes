#leetcodeBaseballgame
#https://leetcode.com/problems/baseball-game/


arr=["1","C","-62","-45","-68"]

result=[]#Stack

for i in range(len(arr)):
    if arr[i]=="+":
        if len(result)>=2:
            result.append(result[-1]+result[-2])
    elif arr[i]=="D":
        if len(result)!=0:
            result.append(result[-1]*2)
    elif arr[i]=="C":
        if len(result)>=1:
            x=result.pop()
    else:
        result.append(int(arr[i]))
print(result)
print(sum(result))