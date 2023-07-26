from heapq import *
nums = [1,3,-1,-3,5,3,6,7]
k = 3


def maxSlidingWindow(nums, k):
    maxHeap = []
    ans = []
    for index, num in enumerate(nums):
        heappush(maxHeap, [-num, index])
        
        if(index < k-1):
            continue
        # print(maxHeap[0][1])
        while(maxHeap[0][1] <= index-k):
            heappop(maxHeap)
        ans.append(-maxHeap[0][0])
    return ans
            

print(maxSlidingWindow(nums, k))