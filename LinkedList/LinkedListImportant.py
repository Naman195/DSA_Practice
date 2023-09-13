class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

# initiualize head and tail pointer with null
class sLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head

        while node:
            yield node

            node = node.next
    
    def insertSll(self, value, location):

        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:

            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:

                tempNode = self.head
                index = 0

                while index < location-1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    def Link(self, head):
        c = []
        cur = head
        while cur:
            c.append(cur.value)
            cur = cur.next

        return c
    def ArraytoLink(self, arr):
        dummy = Node(0)
        ans = dummy
        for i in range(len(arr)):
            ans.next = Node(arr[i])
            ans = ans.next
        return dummy.next



    # Ques 1 = Middle of the LinkedList
    
    def findMiddle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # ques2 = Loop Detect 1
    
    def linkedCyscleI(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            
            fast = fast.next.next
        
            
            if slow == fast:
                return True
        return False
    
    # Ques 3 LinkedList cycle 2
    
    def linkedListCycleII(self, head):
        slow = head
        fast = head
        isLoopDetect = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                isLoopDetect  =True
                break
            
        if isLoopDetect:       
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
                
        return slow
    
    def swapNodes(self, head):
        if head is None or head.next is None:
            return head
        dummy = Node(-1)
        dummy.next = head
        
        prevNode = dummy
        currNode = prevNode.next
        nextNode = currNode.next
        
        while currNode:
            currNode.next = nextNode.next
            nextNode.next = currNode
            prevNode.next = nextNode
            
            prevNode = currNode
            currNode = currNode.next
            nextNode = currNode.next if currNode is not None else None
        return dummy.next
    
    # ques  Reversed a Linkedlkist
    
    def reverse(self, node, prev = None):
        if not node:
            return prev
        temp = node.next
        node.next = prev
        return self.reverse(temp, node)
    
    # Merge Two Sorted Lists
    
    def merge(self, list1, list2):
        dummy = Node(-1)
        dupsDummy = dummy
        
        while list1 and list2:
            if list1.value < list2.value:
                dupsDummy.next = list1
                list1 = list1.next
            else:
                dupsDummy.next = list2
                list2 = list2.next

            dupsDummy = dupsDummy.next
        
        if list1:
            dupsDummy.next = list1
        if list2:
            dupsDummy.next = list2
        return dummy.next
    
    
    # ques Remove Nth node from Lst
    
    def nthNode(self, head, n):
        dummy = Node()
        dummy.next = head
        slow = dummy
        fast = dummy
        
        
        
        for i in range(1, n+1):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next

     
    # ques Add two Numbers
    
    def addNumbers(self, l1, l2):
        dummy = Node()
        temp = dummy
        carry = 0
        
        while l1 or l2 or carry:
            Sum = 0
            
            if l1:
                Sum += l1.value
                l1 = l1.next
            
            if l2:
                Sum += l2.value
                l2 = l2.next
                
            
            Sum += carry
            carry = Sum // 10
            node = Node(Sum%10)
            temp.next = node
            temp = temp.next
        
        return dummy.next
            
    
    
    
            
            

x = sLinkedList()

# arr = [1,2,3,4]
# link = x.ArraytoLink(arr)

# print(x.findMiddle(link).value)
# Z = x.swapNodes(link)
# print(x.Link(Z))

# k = x.reverse(link)
# z = x.Link(k)
# print(z)

# ar1 = [1,5,9,8]
# ar2 = [2,7,15,30]
# link1 = x.ArraytoLink(ar1)
# link2 = x.ArraytoLink(ar2)

# z1 = x.merge(link1, link2)
# k1 = x.Link(z1)
# print(k1)
# m = [1,2,3,4,5]
# n = 2

# n1 = x.nthNode(m, n)
# k1 = x.Link(n1)

# print(k1)

l1 = [2,4,3]
l2 = [5,6,4]

ln1 = x.Link(l1)
ln2 = x.Link(l2)

z = x.addNumbers(ln1, ln2)
k = x.Link(z)

print(k)


