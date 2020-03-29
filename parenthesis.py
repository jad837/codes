# Implement your solution by completing the below function
def isValid(s):
    res = 0
    s=[]#stack
    for i in range(len(s)):
        if s[i]=="(" or s[i] == "{" or s[i]=="[":
            s.append(s[i])
        else:
            if len(s)>0:
                last=s.pop()
                print(last)
                if s[i]==")":
                    if last!="(":
                        return 0
                if s[i]=="}":
                    if last!="{":
                        return 0
                if s[i]=="]":
                    if last!="[":
                        return 0
    if len(s) == 0:
        return 1
    return res

if __name__ == '__main__':
    s = input()
    result = isValid(s)
    if result == 1:
        print('true')
    else:
        print('false')
