import PrintMatrix

# Implement your solution by completing the below function
def traversalPath(matrix, currPosX, currPosY, dirToMove, stepsToMove):
    res = []
    #1->right 2->down 3->left 4->up
    rows = len(matrix)
    column = len(matrix[0])
    if dirToMove == 1:
        if (currPosY + stepsToMove) < column:
            #move right
            i=currPosY+1
            while(stepsToMove>0):
                res.append(matrix[currPosX][i])
                i+=1
                stepsToMove-=1
        else :
            return [-1]
    elif dirToMove == 2:
        if currPosX + stepsToMove < rows:
            #move to down
            
            i=currPosX+1
            while(stepsToMove>0):
                res.append(matrix[i][currPosY])
                i+=1
                stepsToMove-=1
        else :
            return [-1]
    elif dirToMove == 3:
        if currPosY - stepsToMove >= 0:
            #move left
            i=currPosY-1
            while(stepsToMove>0):
                res.append(matrix[currPosX][i])
                i-=1
                stepsToMove-=1
        else :
            return [-1]
    elif dirToMove == 4:
        if currPosX - stepsToMove >= 0:
            #move to up
            i=currPosX-1
            while(stepsToMove>0):
                res.append(matrix[currPosX][i])
                i-=1
                stepsToMove-=1
        else :
            return [-1]
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

    position = input().split()
    currPosX = int(position[0])
    currPosY = int(position[1])
    move = input().split()
    dirToMove = int(move[0])
    stepsToMove = int(move[1])
        
    result = traversalPath(grid, currPosX, currPosY, dirToMove, stepsToMove)
    PrintMatrix.OneDMatrix(result, " ")
    
