from collections import deque

class Node:
    def __init__(self, x, y, time):
        self.x=x
        self.y = y
        self.time = time
    

class Graph:
    # Build a Graph
    
    def buildGraph(self, v, edges):
        graph = [[] for _ in range(v+1)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return graph
    
    
    # DepthFirstSearch Traversal
    
    def DepthFirstSearch(self, v, edges):
        visited = [False]*(v+1)
        graph = self.buildGraph(v, edges)
        lst = []
        for i in range(1, v+1):
            if not visited[i]:
                self.helperFun(graph, i,  visited, lst)
        return lst
    # helper function to do DFS
    
    def helperFun(self, graph,node,  visited, lst):
        visited[node]  = True
        lst.append(node)
        
        for nbr in graph[node]:
            if not visited[nbr]:
                self.helperFun(graph, nbr,visited,lst)
    

    def BreadthFirstSearch(self, v, edges, src):
        visited = [False]*(v+1)
        bfs = []
        
        graph = self.buildGraph(v, edges)
        
        queue = deque()
        queue.append(src)
        visited[src] = True
        
        while queue:
            node=queue.popleft()
            bfs.append(node)
           
            
            for nbr in graph[node]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr] = True
        
        return bfs
    
    
    # RottenOranges
    
    def rottenOranges(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    node  = Node(i, j, 0)
                    queue.append(node)
        
        ans = 0
        
        directions = [[1,0], [0,1],[-1,0],[0,-1]]
        
        
        while queue:
            cur_Node = queue.popleft()
            x, y, time = cur_Node.x, cur_Node.y, cur_Node.time
            
            for direction in directions:
                new_r = x + direction[0]
                new_c = y + direction[1]
                
                if(new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid[new_r][new_c] == 1):
                    grid[new_r][new_c] = 2
                    node = Node(new_r, new_c, time+1)
                    queue.append(node)
                    ans = time+1
            
            
            
            
            # if(x-1 >= 0 and grid[x-1][y] == 1):
            #     grid[x-1][y] = 2
            #     new_Node = Node(x-1, y, time+1)
            #     queue.append(new_Node)
            #     ans = time+1
            # if(y-1 >= 0 and grid[x][y-1] == 1):
            #     grid[x][y-1] = 2
            #     new_Node = Node(x, y-1, time+1)
            #     queue.append(new_Node)
            #     ans = time+1
            # if(x+1 < rows and grid[x+1][y] == 1):
            #     grid[x+1][y] = 2
            #     new_Node = Node(x+1, y, time+1)
            #     queue.append(new_Node)
            #     ans = time+1
            # if(y+1 < cols and grid[x][y+1] == 1):
            #     grid[x][y+1] = 2
            #     new_Node = Node(x, y+1, time+1)
            #     queue.append(new_Node)
            #     ans = time+1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                
        return ans
    
    
    # floodFill
    
    def floodedColor(self, image, sr, sc, color):
        iniColor = image[sr][sc]
        ans = image
        
        self.HelperColor(image, ans, sr, sc, iniColor, color)
        return ans
    
    def HelperColor(self, image, ans, row, col, iniColor, color):
        ans[row][col] = color
        
        n = len(ans)
        m = len(ans[0])
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        for direction in directions:
            new_r = row + direction[0]
            new_c = col + direction[1]
            
            if(new_r >= 0 and new_r < n and new_c >= 0 and new_c < m and image[new_r][new_c] == iniColor and ans[new_r][new_c] != color):
                self.HelperColor(image, ans, new_r, new_c, iniColor, color)
                
    
        
            
            
    def noOfIslands(self, grid):
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        cnt = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]== "1" and not visited[row][col]:
                    cnt += 1
                    self.HelperIsland(row, col, grid, visited)
        return cnt
    
    def HelperIsland(self, row, col, grid, visited):
        visited[row][col] = True
        m = len(grid)
        n = len(grid[0])
        
        queue = deque()
        queue.append((row, col))
        
        directions = [[1,0], [0,1], [-1, 0], [0,-1]]
        for direction in directions:
            new_r = row + direction[0]
            new_c = col + direction[1]
            
            if(new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] == "1" and not visited[new_r][new_c]):
                self.HelperIsland(new_r, new_c, grid, visited)
        
        
    # maxArea Island
    def maxAreaIsland(self, grid):
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        # cnt = 0
        maxArea = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]== 1 and not visited[row][col]:
                    
                    cnt = self.HelperIslandMAxArea(row, col, grid, visited)
                    maxArea = max(maxArea, cnt)
        return maxArea
    
    def HelperIslandMAxArea(self, row, col, grid, visited):
        visited[row][col] = True
        m = len(grid)
        n = len(grid[0])
        c = 1
        
        queue = deque()
        queue.append((row, col))
        
        directions = [[1,0], [0,1], [-1, 0], [0,-1]]
        for direction in directions:
            new_r = row + direction[0]
            new_c = col + direction[1]
            
            if(new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] == 1 and not visited[new_r][new_c]):
                c += self.HelperIslandMAxArea(new_r, new_c, grid, visited)  
        return c
          
            
                    
                    
                    
    
            
            
            
            
        

    


v = 7
edges = [[1,2],[1,5],[2,3],[3,7],[4,6],[4,7],[5,6],[5,7]]
# grid = [[2,1,1],[1,1,0],[0,1,1]]
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
x = Graph()
# print(x.DepthFirstSearch(v, edges))
# print(x.BreadthFirstSearch(v, edges, 1))
# print(x.rottenOranges(grid))
# print(x.floodedColor(image, sr, sc, color))
print(x.maxAreaIsland(grid))
        
                