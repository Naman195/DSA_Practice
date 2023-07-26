from heapq import *
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
 
k = 3


def kthWeakest(mat, k):
    minHeap = []
    for i in range(len(mat)):
        heappush(minHeap, [sum(mat[i]), i])
    print(minHeap)
    ans = []
    for i in range(k):
        Sum, index = heappop(minHeap)
        ans.append(index)
    print(ans)
    
print(kthWeakest(mat, k))
