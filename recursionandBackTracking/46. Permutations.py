nums = [1,2,3]

def printPermutations(nums):
    ans = []
    solve(0, nums, ans)
    return ans
def solve(ind, nums, ans):
    if ind == len(nums):
        ans.append(nums[:])
        return 
    
    for i in range(ind, len(nums)):
        nums[ind], nums[i] = nums[i], nums[ind]
        solve(ind+1, nums, ans)
        nums[ind], nums[i] = nums[i], nums[ind]

print(printPermutations(nums))