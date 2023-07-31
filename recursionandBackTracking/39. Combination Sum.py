candidates = [2,3,6,7]
target = 7

def solve(ind, candidates, target, ps, ans):
    if ind == len(candidates):
        if(target == 0):
            ans.append(list(ps))
        return
    
    if(candidates[ind] <= target):
        ps.append(candidates[ind])
        solve(ind, candidates, target-candidates[ind], ps, ans)
        ps.pop()
    solve(ind+1, candidates, target, ps, ans)
        
    
   
    

def combSum(candidates, target):
    ans = []
    ps = []
    solve(0, candidates, target, ps, ans)
    return ans

print(combSum(candidates, target))

    