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
  
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    
    Dir = "DRLU"
    
    for direction in directions:
        new_row = i + direction[0]
        new_col = j + direction[1]
        
        if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n and not vis[new_row][new_col] and m[new_row][new_col] == 1:
            vis[i][j] = 1
            solve(new_row, new_col, m, n, ans, move+Dir[directions.index(direction)] , vis)
            vis[i][j] = 0
        
    
    
print(findPath(m, N))