class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    
    def levelOrderTraversal(self, root):
        bfs = []
        if root is None:
            return bfs
        
        queue = deque([])
        queue.append(self.root)
        
        while len(queue) != 0:
            level_size = len(queue)
            curr_level = []
            
            for i in range(level_size):
                current = queue.popleft()
                curr_level.append(current.data)
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            
            bfs.append(curr_level[-1])
        return bfs
    

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
# # tree.root.left.right = Node(5)
tree.root.right.left = Node(5)
tree.root.right.left.left = Node(7)
tree.root.right.right = Node(6)
# tree.root.right.left.left = Node(9)
# tree.root.right.right = Node(8)
# print(tree.root.data)
print("level order traversal is: ")
print(tree.levelOrderTraversal(tree.root))



        