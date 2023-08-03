class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    maxi = 0
    
    def __init__(self):
        self.root = None
        
    
    def findHeight(self, root):
        if root is None: return 0
        
        lh = self.findHeight(root.left)
        rh = self.findHeight(root.right)
        
        self.maxi = max(self.maxi, lh+rh)
        return 1 + max(lh, rh)
    
    def diameterofaTree(self, root):
        self.findHeight(root)
        return self.maxi 
    
    
    
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(4)
tree.root.right.left.left = Node(5)
tree.root.right.left.left.left = Node(9)
tree.root.right.right = Node(6)
tree.root.right.right.right = Node(7)
tree.root.right.right.right.right = Node(8)

print(tree.diameterofaTree(tree.root))
        