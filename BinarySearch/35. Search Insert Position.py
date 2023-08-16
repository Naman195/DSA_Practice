
def lowerBound(arr, target):
    low = 0
    high=len(arr)-1
    ans = 0
    while low <= high:
        mid=(low+high)//2
        if arr[mid] >= target:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans

nums = [1,3,5,6]
target = 2

print(lowerBound(nums, target))