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
        
    
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
        return False
    
    def addLeftBoundary(self, root, res):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)
            
            if curr.left: curr = curr.left
            else:
                curr = curr.right
        
    def addrightBoundary(self, root, res):
        curr  = root.right
            
        tmp = []
        while curr:
            if not self.isLeaf(curr):
                tmp.append(curr.data)
            if curr.right :
                curr = curr.right
                    
            else:
                curr = curr.left
        for i in range(len(tmp)-1, -1, -1):
            res.append(tmp[i])
        
    def addLeaves(self, root, res):
        if  self.isLeaf(root):
            res.append(root.data)
            return
        if root.left:
            self.addLeaves(root.left,res)
        if root.right:
            self.addLeaves(root.right, res)
        
    def printBoundary(self, root):
        res = []
        if not root:
            return res
        if not self.isLeaf(root):
            res.append(root.data)
            
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addrightBoundary(root, res)
        return res
        

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

print(tree.printBoundary(tree.root))
                
            