from heapq import *

s = "Aabb"

def frequencySort(s):
    maxHeap = []
    mp = {}
    
    for i in s:
        mp[i] = mp.get(i,0)+1
    # print(mp)


    for key, value in mp.items():
        heappush(maxHeap, (-value,key))
    
    # print(maxHeap)
    ans = []
    while maxHeap:
        
        value, key = heappop(maxHeap)
        
        freq = -value
        
        for i in range(freq):
            ans.append(key)
    
    return "".join(ans)
        
    
print(frequencySort(s))