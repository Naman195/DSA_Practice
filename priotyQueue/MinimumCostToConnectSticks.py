from heapq import *
arr = [2,9,7]

def MinimumCost(arr):
    n=len(arr)
    minHeap = []
    for i in range(n):
        heappush(minHeap, arr[i])
    
    res = 0
    while len(minHeap) > 1:
        x = heappop(minHeap)
        y = heappop(minHeap)
        res += x+y
        heappush(minHeap, x+y)
    return (res)
    
    
        
        
        
    # print(minHeap)
print(MinimumCost(arr))

    