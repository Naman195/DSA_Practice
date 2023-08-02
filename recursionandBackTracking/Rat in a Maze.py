N = 4
m = [[1, 0, 0, 0],
         [1, 1, 0, 1], 
         [1, 1, 0, 0],
         [0, 1, 1, 1]]

def findPath(m, n):
    vis = [[0 for i in range(n)] for j in range(n)]
    ans = []
    
    if m[0][0] == 1:
        solve(0,0, m, n, ans, "", vis)
    return ans

def solve(i,j, m, n, ans, move, vis):
    if i == n-1 and j == n-1:
        ans.append(move)
        return
    
    # downward
    if i+1 < n and not vis[i+1][j] and m[i+1][j] == 1:
        vis[i][j] = 1
        solve(i+1, j, m, n, ans, move + 'D', vis)
        vis[i][j] = 0
    # left
    if j-1 >= 0 and not vis[i][j-1] and m[i][j-1] == 1:
        vis[i][j] = 1
        solve(i, j-1, m, n, ans, move + 'L', vis)
        vis[i][j] = 0
    # right
    if j+1 < n and not vis[i][j+1] and m[i][j+1] == 1:
        vis[i][j] = 1
        solve(i, j+1, m, n, ans, move + 'R', vis)
        vis[i][j] = 0
    # upward
    if i-1 >=0 and not vis[i-1][j] and m[i-1][j] == 1:
        vis[i][j] = 1
        solve(i-1, j, m, n, ans, move + 'U', vis)
        vis[i][j] = 0
    
    
print(findPath(m, N))