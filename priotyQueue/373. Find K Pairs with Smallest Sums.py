from heapq import *
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

def kthPair(nums1, nums2, k):
    minHeap = []
    
    def pushPair(i, j):
        if i < len(nums1) and j < len(nums2):
            heappush(minHeap, (nums1[i]+nums2[j], i, j))
    
    for i in range(len(nums1)):
        pushPair(i, 0)
        
    
    res = []
    
    while k > 0 and minHeap:
        val, x, y = heappop(minHeap)
        res.append([nums1[x], nums2[y]])
        
        k -= 1
        
        pushPair(x, y+1)
    return res
    
print(kthPair(nums1, nums2, k))
    
    