# root = [3,9,20,null,null,15,7]

class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    
    def maxHeight(self, root):
        if root is None:
            return 0
        
        leftH = self.maxHeight(root.left)
        rightH = self.maxHeight(root.right)
        return 1 + max(leftH, rightH)

tree = BinaryTree()
tree.root = Node(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)

# tree.root.right.left.left = Node(9)
# tree.root.right.right = Node(8)
# print(tree.root.data)
# print("level order traversal is: ")
print(tree.maxHeight(tree.root))



        