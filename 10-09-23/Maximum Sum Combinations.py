from heapq import *
A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C = 4

def maxSum(A, B, C):
    ans = []
    for i in range(len(A)):
        # Sum = 0
        for j in range(len(B)):
            Sum = A[i] + B[j]
            ans.append(Sum)
    maxHeap = []
    for i in ans:
        heappush(maxHeap, -i)
    print(maxHeap)
    ans1 = []
    for i in range(C):
        ans1.append(-heappop(maxHeap))
    return ans1

print(maxSum(A, B, C))