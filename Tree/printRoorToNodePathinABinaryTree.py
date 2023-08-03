class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def printPath(self, root, B):
        arr = []
        if root is None:
            return arr
        
        self.getPath(root, B, arr)
        return arr
    
    def getPath(self, root, B, arr):
        
        if root is None:
            return False
        arr.append(root.data)
        
        if root.data == B:
            return True
        if(self.getPath(root.left, B, arr) or self.getPath(root.right, B, arr)):
            return True
        arr.pop()
        return False
    
        
        


tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right = Node(3)
# tree.root.right.right = Node(9)

print(tree.printPath(tree.root, 9))