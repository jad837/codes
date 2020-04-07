#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
#Group Anagrams

def reAnagram(s):
    s = s.lower()
    a=[0]*26
    for i in range(len(s)):
        a[  ord(s[i]) - ord('a') ]+=1
    return str(a)
arr=input().split()
d={}
for i in range(len(arr)):
    l = reAnagram(arr[i])
    if l in d:
        #aid=d.get(l)
        #aid.append(arr[i])
        d[l].append(arr[i])
    else:
        d[l]=[arr[i]]
result=[]
for value in d.values():
    result.append(value)
print (list(d.values()))