from heapq import *

lists = [[1,4,5],[1,3,4],[2,6]]

def mergeK(lists):
    ans = []
    for i in range(len(lists)):
        ans += lists[i]
    
    maxHeap = []
    
    for i in range(len(ans)):
        heappush(maxHeap,ans[i])
    print(maxHeap)
    ans1 = []
    while maxHeap:
        ans1.append(heappop(maxHeap))
    print(ans1)
    
print(mergeK(lists))