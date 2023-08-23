from collections import deque
matrix = [[1, 0, 0], 
          [1, 1, 0], 
          [0, 1, 0]]
def surrounded1(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # queue = deque()
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                bfs(matrix, i, j , visited)
                count += 1
    
    return count

def bfs(matrix, row, col, viisted):
    zero_cnt = 0
    queue = [(row, col)]
    viisted[row][col] = True
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    while queue:
        r, c= queue.pop(0)
        for direction in directions:
            new_r = r + direction[0]
            new_c = c + direction[1]
            
            if(new_r >= 0 and new_r < len(matrix) and new_c >= 0 and new_c > len(matrix[0])):
                if matrix[new_r][new_c] == 0:
                    zero_cnt += 1
                    queue.append((new_r, new_c))
                    viisted[new_r][new_c] = True
    return zero_cnt % 2 == 0

print(surrounded1(matrix))
                
            