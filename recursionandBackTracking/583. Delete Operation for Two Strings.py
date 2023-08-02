word1 = "sea"
word2 = "eat"

def deleteOp(s1, s2):
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
        return solve(m-1, n-1, s1, s2, dp)
    
    left = solve(m-1, n, s1, s2, dp)
    right = solve(m, n-1, s1, s2, dp)
    dp[m][n] = 1 + min(left, right)
    return dp[m][n]
print(deleteOp(word1, word2))