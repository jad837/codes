#HackerearthMarkTheAnswer
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/mark-the-answer-1/

n,md=map(int,input().split())
arr=list(map(int,input().split()))

skip=1
qa=0
i=0
while(i<n and skip>=0):
    if arr[i]<=md:
        qa+=1
    else:
        skip-=1
    i+=1
print(qa)