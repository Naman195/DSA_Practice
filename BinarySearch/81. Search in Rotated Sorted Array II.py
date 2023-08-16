nums = [2,5,6,0,0,1,2]
target = 3
def searRotated(nums, target):
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = (low +high)//2
        
        if nums[mid] == target:
            return True
        
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        
        if(nums[low] < nums[mid]):
            # left is sorted
            if nums[low]<= target and target<= nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            # right is sorted
            if(nums[mid] <= target and target < nums[high]):
                low = mid+1
            else:
                high= mid -1
    return False


print(searRotated(nums, target))
            