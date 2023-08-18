def subsequences(arr):
    ans = []
    solve(0, arr, ans, [])
    return ans

def solve(ind, arr, ans, subL):
    if ind >= len(arr):
        ans.append(list(subL))
        return
    subL.append(arr[ind])
    solve(ind+1, arr, ans, subL)
    subL.remove(arr[ind])
    solve(ind+1, arr, ans, subL)

print(subsequences([3,1,2]))
    