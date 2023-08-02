k = 3

n = 7

def combSum(n, k):
    lst = []
    for i in range(1, 10):
        lst.append(i)
    # print(lst)
    
    ans = []
    ps = []
    solve(0, lst, n, ps, ans)
    return ans

def solve(ind, nums,tar, ps, ans):
    if ind == len(nums):
        if tar == 0:
            ps.sort()
            if len(ps) == k:
                ans.append(list(ps))
        return
    
    if nums[ind] <= tar:
        ps.append(nums[ind])
        solve(ind+1, nums, tar-nums[ind], ps, ans)
        ps.pop()
    
    solve(ind+1, nums, tar, ps, ans)
    
        
print(combSum(n, k))