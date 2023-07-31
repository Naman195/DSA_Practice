nums = [5,2,1]

def solve(ind, nums, ps, lst, n):
    if ind == n:
        lst.append(list(ps))
        return
    
    ps.append(nums[ind])
    solve(ind+1, nums, ps, lst, n)
    ps.pop()
    
    solve(ind+1, nums, ps, lst, n)
    


def findSubsets(nums):
    lst = []
    n = len(nums)
    ps = []
    solve(0, nums, ps, lst, n)
    return lst
print(findSubsets(nums))