#leetcodeMax Increase to Keep City Skyline
#https://leetcode.com/problems/max-increase-to-keep-city-skyline/

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
m=len(grid)
n=len(grid[0])
skylinerow=[]
skylinecol=[]
for i in range(m):
    mr,mc=0,0
    for j in range(n):
        if mr<grid[i][j]:
            mr=grid[i][j]
        if mc<grid[j][i]:
            mc=grid[j][i]
    skylinecol.append(mc)
    skylinerow.append(mr)
for i in range(m):
    for j in range(n):
        if skylinerow[i]< skylinecol[j]:
            grid[i][j] = skylinerow[i]
        if skylinerow[i]>= skylinecol[j]:
            grid[i][j] = skylinecol[j]
