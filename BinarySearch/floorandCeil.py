def ceil(arr, target):
    low = 0
    high = len(arr)-1
    ans = 0
    while low <= high:
        midpoint = (low + high) //2
        if(arr[midpoint] >= target):
            ans = arr[midpoint]
            high = midpoint-1
        else:
            low = midpoint+1
    return ans

# floor()
def floor(arr, target):
    low = 0
    high = len(arr)-1
    ans = -1
    
    while low <= high:
        midpoint = (low +high)//2
        if arr[midpoint] <= target:
            ans = arr[midpoint]
            low = midpoint+1
        else:
            high = midpoint-1
    return ans

            

nums = [1,2,5,6]
target = 3
print(floor(nums, target))