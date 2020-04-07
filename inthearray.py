#inthearray
n,k,x,y = map(int,input().split())
arr=list(map(int,input().split()))
for i in range(n):
    arr[i] = arr[i] % k
arr = sorted(arr)
for i in range(n):
    c=0
    while( arr[i]==arr[i+1] and i<n ):
        i+=1
        c+=1
    
