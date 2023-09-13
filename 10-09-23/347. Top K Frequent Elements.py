from heapq import *
nums = [1,1,1,2,2,3]
k = 2


def topK(nums, k):
    hm = {}
    maxHeap = []
    for i in nums:
        hm[i] = hm.get(i, 0) + 1
    print(hm)
    for key, value in hm.items():
        heappush(maxHeap, (-value, key))
    print(maxHeap)
    ans = []
    for i in range(k):
        ans.append(heappop(maxHeap)[1])
    return ans
        
        

print(topK(nums, k))