
# lowerBound

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


# UpperBound()

def upperBound(arr, target):
    low = 0
    high=len(arr)-1
    ans = 0
    while low <= high:
        mid=(low+high)//2
        if arr[mid] > target:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans
    

arr = [1,2,3,3,5,8,8,10,10,11]
target = 8

print(lowerBound(arr, target))
            
            

