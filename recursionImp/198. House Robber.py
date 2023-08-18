def maxnonAdjacentSum(arr):
    return solve(len(arr)-1, arr)


def solve(ind, arr):
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0
    
    pick = arr[ind] +  solve(ind-2, arr)
    npick = solve(ind-1, arr)
    return max(pick, npick)
nums = [2,7,9,3,1]
print(maxnonAdjacentSum(nums))  