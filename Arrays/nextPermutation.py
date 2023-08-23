nums = [1,2,3]
# nums = [3,2,1]
# nums = [1,1,5]
def generatePermutation(nums):
    ans = []
    solve(0, nums, ans)
    ans.sort()
    # return ans
    x = ans.index(nums)
    print(x)
    if x == len(ans)-1:
        # print()
        
        return ans[x%(len(ans)-1)]
    if ans[x+1] == ans[x]:
        return ans[x+2]
    return ans[x+1]
    
def solve(ind, nums, ans):
    if ind == len(nums):
        ans.append(nums[:])
        return
    
    for i in range(ind, len(nums)):
        nums[i], nums[ind] = nums[ind], nums[i]
        solve(ind+1, nums, ans)
        nums[i], nums[ind] = nums[ind], nums[i]
print(generatePermutation(nums))