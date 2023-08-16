nums = [10,25,99,100]

def findMin(nums):
    low = 0
    high = len(nums)-1
    ans = float('inf')
    while low <= high:
        mid = low + high // 2
        if nums[low] <= nums[mid]:
            # left part is sorted
            
            ans = min(ans, nums[low])
            low = mid+1
        else:
            ans = min(ans, nums[mid])
            high = mid-1
        
        return ans
    
print(findMin(nums))
            
        
    
    