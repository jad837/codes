#https://www.hackerrank.com/contests/launch-assessment-mock-2-batch-1/challenges/the-matrix-reloaded/submissions/code/1322224270
from math import ceil
t=int(input())
while(t>0):
    t-=1
    size=int(input())
    matrix =[]
    for i in range(size):
        row=list(map(int,input().split()))
        matrix.append(row)
    sr,sc=0,0
    m=n=size
    mh=[]
    if size==1:
        print(0)
        continue
    middle=ceil(size//2)
    mid=matrix[middle][middle]
    if mid > matrix[0][0]:
        print(-1)
        continue
    mh.append(matrix[0][0])
    while(sr<m and sc <n):
        for i in range(sc,n):
            if matrix[sr][i] < mh[0] and mid<matrix[sr][i]:
                mh.append(matrix[sr][i])
        sr+=1
        for i in range(sr,m):
            if matrix[i][n-1] < mh[0] and mid<matrix[i][n-1]:
                mh.append(matrix[i][n-1])
        n-=1
        if (sr<m):
            for i in range(n-1,sc-1,-1):
                if matrix[m-1][i] < mh[0] and mid<matrix[m-1][i]:
                    mh.append(matrix[m-1][i])
        m-=1
        if (sc<n):
            for i in range(m-1,sr-1,-1):
                if matrix[i][sc] < mh[0] and mid<matrix[i][sc]:
                    mh.append(matrix[i][sc])
        sc+=1
    print(len(mh))