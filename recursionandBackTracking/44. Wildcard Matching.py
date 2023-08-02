s = "aa"
p = "*"

def unique(p):
    for i in p:
        if i != "*":
            return False
    return True


def wildMatch(s, p):
    dp = []
    for i in range(len(s)+1):
        c= []
        for j in range(len(p)+1):
            c.append(False)
        dp.append(c)
    
    return solve(s, p, len(s), len(p), dp)

def solve(s, p, m, n, dp):
    if m == 0 and n == 0:
        return True
    if n == 0:
        return False
    if m == 0 and unique(p[:n]):
        return  True
    if m == 0:
        return False
    
    if dp[m][n] != -1:
        return dp[m][n]
    
    if s[m-1] == p[n-1] or p[n-1] == "?":
        dp[m][n] = solve(s, p, m-1, n-1, dp)
        return dp[m][n]
    
    if p[m-1] == "*":
        if(solve(s, p, m-1, n, dp) ==  True or solve(s, p, m, n-1, dp) ==  True):
            dp[n][m]  = 1
            return dp[n][m]
    
        dp[m][n] = 0
        return dp[m][n]

    dp[m][n] = 0
    return dp[m][n]
print(wildMatch(s, p))
    
        
    
    