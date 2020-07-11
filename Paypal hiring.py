#Paypal hiring
def swap(string,a,b):
    return string[:a]+string[b]+string[:b]+string[a]+string[:-1]
t = int(input())
while t>0:
    n,k = map(int,input())
    ans =""
    s1=input()
    s2 = input()
    arr=[]
    for i in range(k):
        arr.append((list(map(int,input().split()))))
    arr.sort(key=lambda x :x[0])
    for i in range(n):
        min_index = i
        j=i
        while arr[j][0]==i:
            if s2[arr[j][1]]< s2[min_index]:
                min_index=j
        pass
    t-=1