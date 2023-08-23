# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left, value)
        if value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)
    
    def search(self, value):
        return self.search_recursive(self.root, value)
    
    def search_recursive(self, root, value):
        if root is None or root.data == value:
            return root
        
        if value < root.data:
            return self.search_recursive(root.left, value)
        else:
            return self.search_recursive(root.right, value)
        
bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# print()

print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None
        
        
    