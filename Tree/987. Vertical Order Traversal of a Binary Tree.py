class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def dfs(self,root,  row, col, mp):
        if root is None:
            return
        if col not in mp:
            mp[col] = []
        mp[col].append((row, root.data))
        
        self.dfs(root.left, row+1, col-1, mp)
        self.dfs(root.right, row+1, col+1, mp)
    
    def verticalTraversal(self, root):
        mp= {}
        res = []
        self.dfs(root, 0, 0, mp)
        
        # print(mp)
        
        for col in sorted(mp.keys()):
            column = [val for _, val in sorted(mp[col])]
            res.append(column)
        return res
    
        
        


tree = BinaryTree()
tree.root = Node(3)
tree.root.left = Node(9)
# tree.root.left.left = Node(5)
# tree.root.left.right = Node(3)
tree.root.right = Node(20)
tree.root.right.right = Node(7)
tree.root.right.left = Node(15)

print(tree.verticalTraversal(tree.root))
