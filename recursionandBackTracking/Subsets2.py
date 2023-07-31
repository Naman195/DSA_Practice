arr = [1,2,2]

def solve(ind, nums, ps, fs):
    if ind >= len(nums):
        fs.append(list(ps))
        return
    
    ps.append(nums[ind])
    solve(ind+1, nums, ps, fs)
    ps.pop()
    
    #ignore
    while ind < len(nums)-1 and nums[ind] == nums[ind+1]:
        ind += 1
        continue
    solve(ind+1, nums, ps, fs)

def subsets2(nums):
    ps = []
    fs = []
    
    nums.sort()
    solve(0, nums, ps, fs)
    return fs

print(subsets2(arr))