text1 = "abcde"

text2 = "ace" 

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[-1 for i in range(n+1)] for _ in range(m+1)]
    
    return solve(m, n, s1, s1, dp)
    
    print(dp)

def solve(m, n, s1, s2, dp):
    if m == 0 or n == 0:
        return 0
    
    if dp[m][n] != -1:
        return dp[m][n]
    
    if s1[m-1] == s2[n-1]:
        return  1 + solve(m-1, n-1, s1, s2, dp)
    
    dp[m][n] = max(solve(m-1, n, s1, s2, dp), solve(m, n-1, s1, s2, dp))
    return dp[m][n]    

print(lcs(text1, text2))
    