nums = [-10,-3,0,5,9]

class Node:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None
        
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    
    def sortedArrayToBinarySearchTree(self, nums):
        if not nums:
            return None
        
        mid = len(nums)//2
        
        root = Node(nums[mid])
        root.left = self.sortedArrayToBinarySearchTree(nums[:mid])
        root.right = self.sortedArrayToBinarySearchTree(nums[mid+1:])
        return root

tree = BinaryTree()
x = tree.sortedArrayToBinarySearchTree(nums)
print(x.right.data)