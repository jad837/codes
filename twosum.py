import PrintMatrix

# Implement your solution by completing the below function
def twoSum(nums, target):
    v = [0, 0]
    #nums=sorted(nums)
    if len(nums)<2:
        #print("len<2")
        return v
    number={}
    for i in range(len(nums)): 
        if nums[i] in number:
            return [number.get(nums[i]),i]
        else:
            number[target-nums[i]]=i
    #print(number)
    return v

if __name__ == '__main__':
    n = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    target = int(input())
    result = twoSum(nums, target)
    PrintMatrix.OneDMatrix(result, " ")
    
