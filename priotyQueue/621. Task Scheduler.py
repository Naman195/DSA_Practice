from heapq import *

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

def TaskScheduler(tasks, n):
    mp = {}
    minHeap = []
    for i in tasks:
        mp[i] = mp.get(i, 0)+1

    # print(mp)
    
    for key, value in mp.items():
        heappush(minHeap, value)
    
    res = 0
    while minHeap:
        time = 0
        temp = []
        
        for i in range(n+1):
            if minHeap:
                temp.append(heappop(minHeap)-1)
                # heappop(minHeap)
                time += 1
        
        for t in temp:
            if t:
                heappush(minHeap, t)
        
        res += time if not minHeap else n+1
    return res
                
        
    
    
    
    
    
print(TaskScheduler(tasks, n))     