import PrintMatrix
from operator import itemgetter, attrgetter

def merge(nums):
    res = []
    #print(nums)
    #res = [ [2,5],[1,5] ,[1,7], [3,4],[1,4] ]
    nums = sorted(nums,key=lambda x: x[0])
    #print(nums)
    #consider res as stack
    res.append(nums[0])
    for i in range(1,len(nums)):
        temporal_list = res.pop()
        print("temporal_list"+str(temporal_list))
        print("nums[i]:"+str(nums[i]))
        if temporal_list[1] < nums[i][0]:
            res.append(temporal_list)
            res.append(nums[i])
        elif temporal_list[1] < nums[i][1]:
            temporal_list[1] = nums[i][1]
            res.append(temporal_list)
        else :
            res.append(temporal_list)
        

    return res

if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        row = input().split()
        row = [int(i) for i in row]
        nums.append(row)
    result = merge(nums)
    PrintMatrix.TwoDMatrix(result)
    