from heapq import *

s = "abcabc"
k = 3

def reorganizeString(s, k):
    mp = {}
    minHeap = []
    res = []
    Len = len(s)
    
    for i in s:
        mp[i] = mp.get(i, 0) + 1
    
    for key, value in mp.items():
        heappush(minHeap, (-value, key))  # Use negative values for max-heap behavior
    
    while minHeap:
        temp = []
        cnt = min(k, Len)
        for i in range(cnt):
            if not minHeap: return ""
            val, key = heappop(minHeap)
            res.append(key)
            val += 1  # Increase the count back to positive (as we used negative in heap)
            if val < 0:
                temp.append((val, key))
            Len -= 1
        
        for a in temp:
            heappush(minHeap, a)
    
    return "".join(res) if Len == 0 else ""  # If any characters are left, it's not possible to rearrange

print(reorganizeString(s, k))
