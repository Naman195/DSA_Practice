nums = [1,2,3,1]

def peakEle(nums):
    n = len(nums)
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return nums[n-1]
    
    low = 1
    high = n-2
    
    while low <= high:
        mid_index= (low +high)//2
        if(nums[mid_index] > nums[mid_index-1] and nums[mid_index] > nums[mid_index+1]):
            return mid_index
        elif nums[mid_index]>nums[mid_index -1 ]:
            low = mid_index+1
        else:
            high = mid_index-1
    return nums[low]

print(peakEle(nums))