#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3307/
#Subarray Sum Equals K




from collections import defaultdict 

def subarraysk(arr,target):
    n=len(arr)
    currsum=0
    ps={lambda:0}
    count=0
    for i in range(n):
        currsum+=arr[i]
        if currsum==target:
            count+=1
        if currsum-target in ps:
            count+=ps[currsum-target]

        ps[currsum]+=1
    
    return count

def findSubarraySum(arr, n, Sum):   
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    
    # Sum of elements so far.  
    currsum = 0 
    
    for i in range(0, n):   
    
        # Add current element to sum so far.  
        currsum += arr[i]  

        # If currsum is equal to desired sum,  
        # then a new subarray is found. So  
        # increase count of subarrays.  
        if currsum == Sum:   
            
            res += 1         
    
        # currsum exceeds given sum by currsum  - sum. 
        # Find number of subarrays having   
        # this sum and exclude those subarrays  
        # from currsum by increasing count by   
        # same amount.  
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]  
            
    
        # Add currsum value to count of   
        # different values of sum.  
        prevSum[currsum] += 1 
    print(prevSum)
    return res  
   
if __name__ == "__main__": 
  
    arr =  [-1,-1,1]   
    Sum = 1
    n = len(arr)  
    print(findSubarraySum(arr, n, Sum))  
    print(subarraysk(arr,Sum))  
    