from heapq import *

A = [      [0, 30],
            [5, 10],
            [15, 20]
     ]

def noOfRooms(intervals):
    intervals.sort(key = lambda x : x[0])
    print(intervals)
    heap = []
    res = 0
    for interval in intervals:
        if(len(heap) == 0 or heap[0] > interval[0]):
            res += 1
        else:
            heappop(heap)
        heappush(heap, interval[1])
    return res


print(noOfRooms(A))
    