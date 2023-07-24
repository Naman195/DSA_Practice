from heapq import *
points = [[1,3],[-2,2]]
k = 1


def kthClosestOrigin(points, k):
    maxHeap = []
    
    for i in range(len(points)):
        
        x = points[i][0]
        y = points[i][1]
        
        dis = x*x + y*y
        
        heappush(maxHeap, (-dis, x, y))
        if(len(maxHeap) == k+1):
            heappop(maxHeap)
    ans = []
    while maxHeap:
        dis, x, y  = heappop(maxHeap)
        ans.append([x, y])
    return ans

print(kthClosestOrigin(points, k))
        
            
    