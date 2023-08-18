def solve(ind, arr, ans):
    if ind == len(arr):
        ds = []
        for i in range(len(arr)):
            ds.append(arr[i])
        
        ans.append(list(ds))
        return
    
    for i in range(ind, len(arr)):
        arr[i], arr[ind] = arr[ind], arr[i]
        
        solve(ind+1, arr, ans)
        arr[i], arr[ind] = arr[ind], arr[i]

def permutations(arr):
    ans= []
    solve(0, arr, ans)
    return ans
print(permutations([1,2,3]))
        
    