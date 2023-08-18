def permutations(arr):
    n = len(arr)
    freq = [0]*n
    ans = []
    ds = []
    solve(arr, ds, ans, freq)
    return ans


def solve(arr, ds, ans, freq):
    if len(ds) == len(arr):
        ans.append(list(ds))
        return
    
    for i in range(len(arr)):
        if freq[i] != True:
            freq[i] = True
            ds.append(arr[i])
            solve(arr, ds, ans, freq)
            ds.pop()
            
            freq[i] = False
            
print(permutations("12"))