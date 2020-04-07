from collections import defaultdict
J="aA"
S="aAAbbbb"
s=defaultdict(S)
count=0
for key,value in s.items():
    if key in J:
        count+=s[key]
print( count)