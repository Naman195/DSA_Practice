nums = [3,2,1,5,6,4]
k = 2


from heapq import *

def kthLargest(nums, k):
    minHeap = []
    for i in range(len(nums)):
        heappush(minHeap, nums[i])
        
        if(len(minHeap) == k+1):
            heappop(minHeap)
    
    
# print(kthLargest(nums, k))

    ans = []
    while minHeap:
        ans.append(heappop(minHeap))
    return ans[0]


print(kthLargest(nums, k))
