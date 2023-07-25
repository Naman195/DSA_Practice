from heapq  import *

trips = [[2,1,5],[3,3,7]]
capacity = 5


def CarPooling(trips, capacity):
    minHeap = []
    
    
    for i in range(len(trips)):
        heappush(minHeap, (trips[i][1], trips[i][0]))
        heappush(minHeap, (trips[i][2], -trips[i][0]))
    onBoarding = 0
    
    while minHeap:
        onBoarding += heappop(minHeap)[1]
        # print(onBoarding)
        if(onBoarding > capacity):
            return False
    return True

        

print(CarPooling(trips, capacity))