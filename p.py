
# Implement your solution by completing the below function
def numIslands(grid):
    x = 0
    #print(grid)
    visited=[ [False]*len(grid[0]) ]*len(grid)
    print(visited)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1' and not visited[i][j]:
                x+=1
                search_I(grid,i,j,visited)
    return x

def search_I(grid,i,j,visited):
    if ( i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=='0' or visited[i][j]==True):
        return 
    visited[i][j]=True
    search_I(grid,i+1,j,visited)
    search_I(grid,i-1,j,visited)
    search_I(grid,i,j+1,visited)
    search_I(grid,i,j-1,visited)


if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        r = input()
        grid.append(r)
    result = numIslands(grid)
    print(result)
