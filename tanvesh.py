
t = int(input())

for _ in range(t):
    track = [0] * 102
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        track[arr[i]] = 1
    count = None
    for i in range(1, 102):
        if track[i] == 1: 
            count = i
            continue
        if track[i] != 1 and x == 0: break
        elif track[i] == 0 and x > 0:
            count = i
            track[i] = 1
            x -= 1
    
    print(count )
