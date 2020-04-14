#https://leetcode.com/problems/backspace-string-compare/
#leetcode backspace string compare
def isNotEmpty(a):
    if len(a)>0:
        return True
    return False
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i=0
        s=[]
        t=[]
        while(i<len(S) and i<len(T)):
            if S[i]=="#" :
                if isNotEmpty(s) :
                    s.pop()
                #s.pop()
            else:
                s.append(S[i])
            if T[i]=="#" :
                if isNotEmpty(t):
                    t.pop()
                #t.pop()
            else:
                t.append(T[i])
            i+=1
        while(i<len(S)):
            if S[i]=="#" :
                if isNotEmpty(s):
                    s.pop()
                #s.pop()
            else:
                s.append(S[i])
            i+=1
        while (i<len(T)):
            if T[i]=="#" :
                if isNotEmpty(t):
                    t.pop()
            else:
                t.append(T[i])
            i+=1
        #print(s)
        #print(t)
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
        else:
            return False
        return True

S="a##c"
T="#a#c"

#S="y#fo##f"
#T="y#f#o##f"
x=  Solution()
print(x.backspaceCompare(S,T) )