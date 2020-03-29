#leetcode_validanagram
#https://leetcode.com/problems/valid-anagram/

def isAnagram(s,t):
    if len(s)!=len(t):
            return False
    anagram={}
    for i in range(len(s)):
        if s[i] not in anagram:
            anagram[s[i]]=1
        else:
            anagram[s[i]]+=1
    for i in range(len(t)):
        if t[i] in anagram:
            if anagram[t[i]]>0:
                anagram[t[i]]-=1
            else:
                return False
        else:
            return False
    return True
s="anagram"
t="nagaram"
print(isAnagram(s,t))
