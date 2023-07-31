candidates = [10,1,2,7,6,1,5]
target = 8

def combSum2(candidates, target):
    ps = []
    fs = []
    solve(0, candidates, target, ps, fs)
    return fs

def solve(ind, nums, target, ps, fs):
    if(ind == len(nums)):
        if target == 0:
            ps.sort()
            if ps not in fs:
                fs.append(list(ps))
    
        return
    
    
    if(nums[ind] <= target):
        ps.append(nums[ind])
        solve(ind+1, nums, target-nums[ind], ps, fs)
        ps.pop()
    
    solve(ind+1, nums, target, ps, fs)
    

print(combSum2(candidates, target))