nums = [5,2,1]

def solve(ind, nums, ps, lst, lst2,  n, sum1):
    if ind == n:
        lst.append(list(ps))
        lst2.append(sum1)
        return
    
    ps.append(nums[ind])
    solve(ind+1, nums, ps, lst, lst2,  n, sum1 + nums[ind])
    ps.pop()
    
    solve(ind+1, nums, ps, lst,lst2,  n, sum1)
    


def findSubsets(nums):
    lst = []
    n = len(nums)
    lst2 = []
    ps = []
    solve(0, nums, ps, lst, lst2, n, 0)
    lst2.sort()
    return lst, lst2
print(findSubsets(nums))