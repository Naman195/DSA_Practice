class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    
    def searinABinarySearchTree(self, root, val):
        if root is None:
            return root
        if root.data == val:
            return root
        
        if  root.data < val:
            return self.searinABinarySearchTree(root.right, val)
        else:
            return self.searinABinarySearchTree(root.left, val)
        

tree = BinaryTree()
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right = Node(7)
# tree.root.right.right = Node(9)

x = tree.searinABinarySearchTree(tree.root, 2)
print(x.left.data)
