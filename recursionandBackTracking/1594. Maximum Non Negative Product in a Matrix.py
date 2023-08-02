grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
import math
class ProdUct:
    def maxProdUct(self, grid):
        def solve(row,col,grid,prod):
            if row>=len(grid) or col>=len(grid[0]):
                return
            if grid[row][col]==0:
                self.maxProd=max(self.maxProd,0)
                return

            if (row==len(grid)-1 and col==len(grid[0])-1):
                self.maxProd=max(self.maxProd,prod*grid[row][col])
                return
            solve(row+1,col,grid,prod*grid[row][col])
            solve(row,col+1,grid,prod*grid[row][col])  
    


        if len(grid)==1 and len(grid[0])==1:
            return grid[0][0]
        self.maxProd=-math.inf
        solve(0,0,grid,1)
        if self.maxProd>=0:
            return (self.maxProd)%(1000000007)
        else:
            return -1

x = ProdUct()
print(x.maxProdUct(grid))
