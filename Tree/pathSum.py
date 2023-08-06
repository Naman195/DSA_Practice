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
    
    def hasPathSum(self, root, target):
        return self.solve(root, target, 0)
    
    def solve(self, root, target, iSum):
        if not root:
            return
        if root.left is None and root.right is None:
            iSum += root.data
            
            if(iSum == target):
                return True
        return self.solve(root.left, target, iSum+root.data) or self.solve(root.right, target, iSum + root.data)
tree = BinaryTree()
tree.root = Node(5)
tree.root.left = Node(4)
tree.root.left.left = Node(11)
tree.root.left.left.left = Node(7)
tree.root.left.left.right = Node(2)
tree.root.right = Node(8)
tree.root.right.right = Node(4)
tree.root.right.right.left = Node(1)
tree.root.right.left = Node(13)

print(tree.hasPathSum(tree.root, 22))