class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        selfright = None


def allTraversal(root):
    pre = []
    in_order = []
    post = []
    stack = [(root, 1)]
    
    if root is None:
        return pre,in_order,post
    
    while stack:
        node, state = stack.pop()
        
        # part of preOrderTraversal
        if state == 1:
            
            pre.append(node.data)
            state += 1
            stack.append((node, state))
            
            if node.left:
                stack.append((node.left, 1))
        
        # part of in_Order
        
        elif state == 2:
            
            in_order.append(node.data)
            state += 1
            stack.append((node, state))
            
            if node.right:
                stack.append((node.right, 1))
        
        else:
            post.append(node.data)
    return pre, in_order, post

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    
    pre_order, in_order, post_order = allTraversal(root)
    print("Pre_order", pre_order)
    print("in_order", in_order)
    print("Post_order", post_order)
            