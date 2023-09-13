from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BinaryTRee:
    
    def __init__(self):
        self.root = None
    
    def levelOrder(self, root):
        bfs = []
        if not root:
            return bfs
        
        queue = deque([])
        queue.append(self.root)
        
        while queue:
            size = len(queue)
            current_level = []
            for i in range(size):
                current = queue.popleft()
                current_level.append(current.data)
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            if len(current_level) == 1:
                bfs.append(current_level[0])
            else:
                
                bfs.append(current_level[0])
                bfs.append(current_level[-1])
        return  bfs


tree = BinaryTRee()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
# tree.root.right.left.left = Node(7)
tree.root.right.right = Node(7)
# tree.root.right.left.left = Node(9)
# tree.root.right.right = Node(8)

                
            
print("leftMost and rightMost nodes is", tree.levelOrder(tree.root))