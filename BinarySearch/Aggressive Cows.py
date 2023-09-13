arr = [4,2,1,3,6]
k = 2

def canWePlace(arr, cows, dist):
    last = arr[0]
    cntCows = 1
    
    for i in range(1, len(arr)):
        if arr[i]- last >= dist:
            last = arr[i]
            cntCows += 1
        if cntCows >= cows:
            return True
        
    return False
def aggresiveCows(arr, k):
    arr.sort()
    low = 1
    high = arr[len(arr)-1] - arr[0]
    
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(arr, k, mid):
            low = mid+1
        else:
            high = mid-1
    return high
print(aggresiveCows(arr, k))


    
        