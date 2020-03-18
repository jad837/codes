
# Implement your solution by completing the below function
def numIslands(grid):
    x = 0
    #print(grid)
    if len(grid)<=0:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='1':
                x+=1
                search_I(grid,i,j)
    return x

def search_I(grid,i,j):
    if ( i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=='0' ):
        return 
    string=grid[i]
    string=string[:j]+"0"+string[j+1:]
    grid[i]=string
    search_I(grid,i+1,j)
    search_I(grid,i-1,j)
    search_I(grid,i,j+1)
    search_I(grid,i,j-1)


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
