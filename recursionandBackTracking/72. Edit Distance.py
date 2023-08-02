word1 = "horse"
word2 = "ros"


def edit(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[-1 for i in range(n+1)] for _ in range(m+1)]
    return solve(m, n, s1, s2, dp)

def solve(m, n, s1, s2, dp):
    if m == 0:
        return n
    if n == 0:
        return m
    if dp[m][n] != -1:
        return dp[m][n]
    
    if s1[m-1] == s2[n-1]:
        dp[m][n] = solve(m-1, n-1, s1, s2, dp)
        return dp[m][n]
    
    insert = solve(m, n-1, s1, s2, dp)
    delete = solve(m-1, n, s1, s2, dp)
    replace = solve(m-1, n-1, s1, s2, dp)
    
    dp[m][n] = 1 + min(insert, min(delete, replace))
    return dp[m][n]

print(edit(word1, word2))
        
    
    