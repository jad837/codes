t = int(input())

result = []
for _ in range(t):

    inp = []
    n =  int(input())
    for _ in range(n):
        inp.append(input().split('*')[1])

    maxString = (max(inp, key = len))
    #print(maxString)
    flag = True    
    for x in inp:
        if maxString.find(x) == -1:
            flag = False
            break

    if flag:
        result.append(maxString)
    else:
        result.append('*')

for i in range(t):
    print("Case #"+str(i+1)+":", result[i], sep = " ")