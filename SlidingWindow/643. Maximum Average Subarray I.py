nums = [1,12,-5,-6,50,3]
k = 3

def maxAverage(nums, k):
    i = 0
    j = 0
    wSum = 0
    wAvg = float('-inf')
    
    while(j < len(nums)):
        wSum += nums[j]
        if(j >= k-1):
            wAvg = max(wAvg, (wSum/k))
            wSum -= nums[i]
            i += 1
        j += 1
    return wAvg
print(maxAverage(nums, k))