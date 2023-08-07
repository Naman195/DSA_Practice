inp = "abcabcbb"

def passwordStrengthChecker(s):
    maxStrength = 0
    currStrength = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            currStrength = 1
        else:
            currStrength += 1
            maxStrength = max(maxStrength, currStrength)
    
    return maxStrength

print(passwordStrengthChecker(inp))
