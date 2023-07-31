class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
    
    def reverseLinkedList(self, head):
        dummy = None
        while head:
            nextNode = head.next
            head.next = dummy
            dummy = head
            head = nextNode
        return dummy


head = [1,2,3,4,5]
ob = SinglyLinkedList()
print(ob.reverseLinkedList(head))
        
    