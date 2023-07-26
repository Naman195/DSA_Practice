from heapq import *

words = ["i","love","leetcode","i","love","coding"]
k = 2
def topKFrequentWords(words, k):
    mp = {}
    minHeap = []
    for i in words:
        mp[i] = mp.get(i, 0)+1
    
    for key, value in mp.items():
        heappush(minHeap, (-value, key))
       
    print(minHeap)  
    ans = []
    while minHeap:
        val, key = heappop(minHeap)
        
        ans.append(key)
    return ans
        
        
    # print(mp)
    
print(topKFrequentWords(words, k))