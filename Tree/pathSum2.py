class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    

    
class BinaryTree:
   
    
    def __init__(self):
        self.root = None
    
    def hasPathSum(self, root, target):
        res = []
        path = []
        self.solve(root, target, 0, path, res)
        return res
    def solve(self, root, target, iSum, path, res):
        if not root:
            return 
        iSum += root.data
        path.append(root.data)
        
        if(iSum == target and root.left is None and root.right is None):
            res.append(list(path))
            
        self.solve(root.left, target, iSum, path, res)
        self.solve(root.right, target, iSum, path, res)
        path.pop()
        iSum -= root.data
        
        
        
            
       
tree = BinaryTree()
tree.root = Node(5)
tree.root.left = Node(4)
tree.root.left.left = Node(11)
tree.root.left.left.left = Node(7)
tree.root.left.left.right = Node(2)
tree.root.right = Node(8)
tree.root.right.right = Node(4)
tree.root.right.right.left = Node(5)
tree.root.right.right.right = Node(1)
tree.root.right.left = Node(13)

print(tree.hasPathSum(tree.root, 22))