class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def dfs(self, root, row, col, mp):
        if root is None:
            return
        if col not in mp:
            mp[col] = [(row, root.data)]
        else:
            # Update only if the current node is at a lower level (closer to the bottom)
            if row >= mp[col][0][0]:
                mp[col] = [(row, root.data)]

        self.dfs(root.left, row + 1, col - 1, mp)
        self.dfs(root.right, row + 1, col + 1, mp)
    
  
    def bottomView(self, root):
        mp = {}
        self.dfs(root, 0, 0, mp)
        # print(mp)

        res = []
        for col in sorted(mp.keys()):
            # Get the last tuple in the list at mp[col]
            last_tuple = mp[col][-1]
            res.append(last_tuple[1])
        return res
        
        
    
        
        


tree = BinaryTree()
tree.root = Node(3)
tree.root.left = Node(9)
# tree.root.left.left = Node(5)
# tree.root.left.right = Node(3)
tree.root.right = Node(20)
tree.root.right.right = Node(7)
tree.root.right.left = Node(15)

print(tree.bottomView(tree.root))
