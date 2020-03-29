n , x = map(int , input().strip().split())
s = input().strip()
count=0
se=set()
if n<2:
    if int(s,2)>=x:
        se.add(s)
else:
    for i in range(n):
        string=""
        for j in range(i,n):
            string+=s[j]
            if int(string,2) >= x:
                se.add(string)
print(se)
print(len(se))
print(int("1111111111111111111111111111111",2))