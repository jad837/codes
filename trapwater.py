# Implement your solution by completing the below function
def trap(heights):
    ans = 0
    length=len(heights)
    left=[0]*length
    right=[0]*length
    left[0]=heights[0]
    for i in range(1,length):
        left[i]=max(left[i-1],heights[i])
    right[n-1]=heights[n-1]
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],heights[i])
    
    for i in range(n):
        ans+=min(right[i],left[i])-heights[i]
    return ans

if __name__ == '__main__':
    n = int(input())
    heights = []
    if (n != 0):
        heights = input().split()
        heights = [int(i) for i in heights]
    result = trap(heights)
    print(result)
    
