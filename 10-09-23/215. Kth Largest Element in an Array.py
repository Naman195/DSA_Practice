from heapq import *
nums = [3,2,1,5,6,4]
k = 2

def kthLargest(nums, k):
    
    maxHeap = []
    for i in range(len(nums)):
        heappush(maxHeap, -nums[i])
    
    ans = []
    for i in range(k):
        ans.append(-heappop(maxHeap))
    
    print(ans[-1])
    
print(kthLargest(nums, k))