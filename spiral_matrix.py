import PrintMatrix

# Implement your solution by completing the below function
def spiralOrder(matrix):
    res = []
    r_s,c_s=0,0
    m=len(matrix)
    n=len(matrix[0])
    while ( r_s <m and c_s < n):
        print("row_start"+str(r_s)+"row_end"+str(m)+"column_start"+str(c_s)+"column_end"+str(n))
        i = c_s
        while ( i < n):
            res.append( matrix[r_s][i] )
            i+=1
        r_s+=1
        j = r_s
        while (j < m):
            res.append( matrix[j][n-1] )
            j+=1
        n-=1
        i = n-1
        while( i >= c_s  ):
            res.append( matrix[m-1][i] )
            i-=1
        m-=1
        j = m-1
        while( j >= r_s):
            res.append( matrix[j][c_s] )
            j-=1
        c_s+=1
    return res

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        grid.append(nums)
    result = spiralOrder(grid)
    PrintMatrix.OneDMatrix(result, " ")
    
