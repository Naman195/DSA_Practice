from heapq import *
nums = [3,2,1,5,6,4]
k = 2


def kthSmalllest(nums, k):
    maxHeap = []
    for i in range(len(nums)):
        heappush(maxHeap, -nums[i])
        
        if(len(maxHeap) == k+1):
            heappop(maxHeap)
    
    
# print(kthLargest(nums, k))

    ans = []
    while maxHeap:
        ans.append(-heappop(maxHeap))
    return ans[0]

print(kthSmalllest(nums, k))