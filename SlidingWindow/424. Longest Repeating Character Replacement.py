s = "ABAB"
k = 2


def longestRepeatingChar(s, k):
    mp = {}
    res = 0
    l = 0
    maxF = 0
    n = len(s)
    
    for r in range(n):
        mp[s[r]] = mp.get(s[r], 0) + 1
        
        maxF = max(maxF, mp[s[r]])
        
        while (r-l+1) - maxF > k:
            mp[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res

print(longestRepeatingChar(s, k))
            