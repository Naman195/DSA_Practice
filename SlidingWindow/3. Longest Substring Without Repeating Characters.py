s = "abcabcbb"

def lenofLongestSubstring(s):
    if s == None or len(s) == 0:
        return 0
    
    wst = 0
    maxLen = 0
    mp = {}
    for wEnd in range(len(s)):
        rightChar = s[wEnd]
        if rightChar in mp:
            wst = max(wst, mp[rightChar]+1)
        mp[rightChar] = wEnd
        
        maxLen = max(maxLen, wEnd-wst+1)
    return maxLen

print(lenofLongestSubstring(s))