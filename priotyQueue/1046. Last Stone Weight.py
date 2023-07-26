from heapq import *
stones = [2,7,4,1,8,1]

def maxStone(stones):
    maxHeap = []
    for i in range(len(stones)):
        heappush(maxHeap,-stones[i])
    
    while  len(maxHeap) > 1:
        x = -heappop(maxHeap)
        y = -heappop(maxHeap)
        
        if x == y:
            continue
        else:
            heappush(maxHeap, -(x-y))
    
    if len(maxHeap) == 1:
        return -heappop(maxHeap)
    else:
        return 0
    
print(maxStone(stones))
        
    