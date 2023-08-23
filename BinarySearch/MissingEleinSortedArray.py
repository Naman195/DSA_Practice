nums = [4,7,9,10]
k = 1

def missingEle(nums, k):
    noOfMissingEle = 0
    start = 0
    end = len(nums)-1
    
    while start <= end:
        mid = (start + end)//2
        
        noOfMissingEle = nums[mid] - nums[0] - mid
        if noOfMissingEle <= k:
            start = mid+1
        else:
            end = mid-1
        
    if(noOfMissingEle < k):
        return nums[end] + (k - noOfMissingEle)
    else:
        return nums[start] - (noOfMissingEle - k) - 1
        
print(missingEle(nums, k))