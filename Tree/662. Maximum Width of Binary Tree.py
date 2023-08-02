class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
from collections import deque
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    
    def maxWidth(self, root):
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_size = len(queue)
            _, level_Start = queue[0]
            
            for i in range(level_size):
                node, index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right,2*index+1 ))
            max_width = max(max_width, index-level_Start+1)
        return max_width
    
    
    

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(3)
tree.root.left.left = Node(5)
tree.root.left.right = Node(3)
tree.root.right = Node(2)
tree.root.right.right = Node(9)

print("level order traversal is: ")
print(tree.maxWidth(tree.root))



        