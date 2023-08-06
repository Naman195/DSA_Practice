class Stack:
    
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0]*self.size
    
    
    def Push(self, el):
        self.top  += 1
        self.arr[self.top] = el
    
    def Pop(self):
        x = self.arr[self.top]
        self.top -= 1
        return x
    
    def Top(self):
        return self.arr[self.top]
    
    def Size(self):
        return self.top + 1

ob = Stack()
ob.Push(2)
ob.Push(20)
ob.Push(3)

print(ob.Size())
ob.Pop()
print(ob.Size())