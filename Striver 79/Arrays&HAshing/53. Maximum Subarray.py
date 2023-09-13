nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    maxSum = float('-inf')
    curSum = 0
    
    for i in range(len(nums)):
        curSum += nums[i]
        
        if maxSum < curSum:
            maxSum = curSum
        
        if curSum < 0:
            curSum = 0
    return maxSum

print(maxSubArray(nums))
        
        
            
            
            