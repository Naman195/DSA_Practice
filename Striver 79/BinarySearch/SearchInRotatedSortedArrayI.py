nums = [4,5,6,7,0,1,2]
target = 2

def sortedArray(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == target:
            return mid
        
        
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid-1
                
            else:
                low = mid+1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
    
    return -1

print(sortedArray(nums, target))